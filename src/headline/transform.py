import logging
from typing import Callable, Dict, List, Optional, Tuple

import libcst as cst

from headline import io
from headline import sorters as srt
from headline.transformers.func_transformers import FuncTransformer
from headline.utils import strip_test_prefix_suffix
from headline.visitors.func_visitors import FuncVisitor

from ._logger import compress_logging_value

logger = logging.getLogger()


def sort_src_funcs_and_tests(
    src_path: str,
    test_path: Optional[str],
    inp_sort_type: str,
    inp_tests_only: bool,
    inp_rename: bool,
    suffix: str = "",
) -> bool:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    save_src_res = save_test_res = True

    src_code = io.get_src_code(src_path)
    src_tree: cst.Module = cst.parse_module(src_code)

    if inp_tests_only:
        if inp_rename:
            raise ValueError(
                "inp_tests_only and inp_rename can't both be true. "
                f"[inp_tests_only, inp_rename]: [{inp_tests_only}, {inp_rename}]"
            )
        name_changes = {}
    else:
        src_tree, name_changes = sort_src_funcs(
            src_tree, _get_sort_type(inp_sort_type), rename_funcs=inp_rename
        )

    if test_path:
        test_code = io.get_src_code(test_path)
        test_tree = cst.parse_module(test_code)
        test_tree = sort_test_funcs(test_tree, src_tree, name_changes)
        test_save_path = test_path.replace(".py", f"{suffix}.py")
        save_test_res = io.save_modified_code(test_tree.code, test_save_path)

    src_save_path = src_path.replace(".py", f"{suffix}.py")
    save_src_res = io.save_modified_code(src_tree.code, src_save_path)

    return all([save_src_res, save_test_res])


def sort_src_funcs(
    src_tree: cst.Module,
    sorting_func: Optional[Callable] = None,
    sorted_funcs: Optional[List[str]] = None,
    rename_funcs: bool = False,
) -> Tuple[cst.Module, Dict[str, str]]:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    if all([sorting_func is None, sorted_funcs is None]):
        raise ValueError("Must have either sorting_func or sorted_funcs")

    fv = _get_visitor(src_tree)

    if sorted_funcs is None and isinstance(sorting_func, Callable):
        sorted_funcs = sorting_func(fv.func_defs.values())

    transformer = FuncTransformer(
        fv.func_defs,
        sorted_funcs,  # type: ignore
        rename_funcs=rename_funcs,
        classes_methods=fv.classes_methods,
    )
    modified_tree = src_tree.visit(transformer)
    return modified_tree, transformer.name_changes


def sort_test_funcs(
    test_tree: cst.Module,
    src_tree: cst.Module,
    call_name_changes: Dict[str, str],
) -> cst.Module:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    test_func_defs = _get_visitor(test_tree).func_defs

    normed_test_func_defs = {
        strip_test_prefix_suffix(k): v for k, v in test_func_defs.items()
    }

    fv = _get_visitor(src_tree)
    func_defs = [f.strip("_") for f in fv.top_level_funcs]
    sorted_test_order = [
        f for f in func_defs if f in normed_test_func_defs.keys()
    ]

    transformer = FuncTransformer(
        normed_test_func_defs,
        sorted_test_order,  # type: ignore
        rename_funcs=False,
        apply_name_changes=bool(call_name_changes),
        is_test_file=True,
        classes_methods=fv.classes_methods,
    )
    transformer.name_changes = call_name_changes
    modified_tree = test_tree.visit(transformer)
    return modified_tree


def _get_sort_type(inp_sort_type: str) -> Callable:
    sort_types = {
        "newspaper": srt.sort_funcs_newspaper,
        "called": srt.sort_funcs_called,
        "calls": srt.sort_funcs_calls,
        "alphabetical": srt.sort_funcs_alphabetical,
        "alphabetical_include_leading_underscores": srt.sort_funcs_alphabetical_inc_leading_underscores,
    }
    if inp_sort_type in sort_types:
        return sort_types[inp_sort_type]
    raise KeyError(f"sort type {inp_sort_type} is not implemented")


def _get_visitor(src_module: cst.Module) -> FuncVisitor:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    src_visitor = FuncVisitor()
    src_module.visit(src_visitor)
    src_visitor.process_func_defs()
    return src_visitor

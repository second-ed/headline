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


def _get_src_module(src_path: str) -> cst.Module:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    src_code = io.get_src_code(src_path)
    src_module = cst.parse_module(src_code)
    return src_module


def _get_visitor(src_module) -> FuncVisitor:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    src_visitor = FuncVisitor()
    src_module.visit(src_visitor)
    src_visitor.process_func_defs()
    return src_visitor


def sort_src_funcs(
    src_path: str,
    sorting_func: Optional[Callable] = None,
    sorted_funcs: Optional[List[str]] = None,
    rename_funcs: bool = False,
) -> Tuple[str, Dict[str, str]]:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    if all([sorting_func is None, sorted_funcs is None]):
        raise ValueError("Must have either sorting_func or sorted_funcs")

    src_module = _get_src_module(src_path)
    func_defs = _get_visitor(src_module).func_defs

    if sorted_funcs is None and isinstance(sorting_func, Callable):
        sorted_funcs = sorting_func(func_defs.values())

    transformer = FuncTransformer(
        func_defs,
        sorted_funcs,  # type: ignore
        rename_funcs=rename_funcs,
    )
    modified_tree = src_module.visit(transformer)
    return modified_tree.code, transformer.name_changes


def sort_test_funcs(
    test_path: str,
    src_code: str,
    call_name_changes: Dict[str, str],
) -> str:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    test_module = _get_src_module(test_path)
    test_func_defs = _get_visitor(test_module).func_defs

    normed_test_func_defs = {
        strip_test_prefix_suffix(k): v for k, v in test_func_defs.items()
    }

    src_module = cst.parse_module(src_code)
    func_defs = [
        f.strip("_") for f in _get_visitor(src_module).top_level_funcs
    ]
    sorted_test_order = [
        f for f in func_defs if f in normed_test_func_defs.keys()
    ]

    transformer = FuncTransformer(
        normed_test_func_defs,
        sorted_test_order,  # type: ignore
        rename_funcs=False,
        apply_name_changes=bool(call_name_changes),
        is_test_file=True,
    )
    transformer.name_changes = call_name_changes
    modified_tree = test_module.visit(transformer)
    return modified_tree.code


def sort_src_funcs_and_tests(
    src_path: str,
    test_path: str,
    inp_sort_type: str,
    inp_tests_only: bool,
    inp_rename: bool,
    suffix: Optional[str] = None,
):
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    sort_types = {
        "newspaper": srt.sort_funcs_newspaper,
        "called": srt.sort_funcs_called,
        "calls": srt.sort_funcs_calls,
        "alphabetical": srt.sort_funcs_alphabetical,
        "alphabetical_include_leading_underscores": srt.sort_funcs_alphabetical_inc_leading_underscores,
    }

    if inp_tests_only:
        src_code = io.get_src_code(src_path)
        name_changes = {}
    else:
        src_code, name_changes = sort_src_funcs(
            src_path, sort_types[inp_sort_type], rename_funcs=inp_rename
        )

    test_code = sort_test_funcs(test_path, src_code, name_changes)

    if suffix:
        src_save_path = src_path.replace(".py", f"_{suffix}.py")
        test_save_path = test_path.replace(".py", f"_{suffix}.py")
    else:
        src_save_path = src_path
        test_save_path = test_path

    io.save_modified_code(src_code, src_save_path)
    io.save_modified_code(test_code, test_save_path)
    return True

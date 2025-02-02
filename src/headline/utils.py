import logging
import re
from typing import Dict

import black
import isort
import libcst as cst

from ._logger import compress_logging_value

logger = logging.getLogger()


def get_func_name_edit(
    func_name: str, all_funcs: list[str], private_funcs: list[str]
) -> str:
    logger.debug({key: compress_logging_value(val) for key, val in locals().items()})
    if is_not_private_and_has_leading_underscore(func_name, all_funcs, private_funcs):
        return func_name.lstrip("_")
    if is_private_and_has_no_leading_underscore(func_name, all_funcs, private_funcs):
        return f"_{func_name}"
    return ""


def get_normed_test_key(item: str, is_test: bool) -> str:
    if is_test:
        return strip_test_prefix_suffix(item)
    return item


def str_to_cst(code: str) -> cst.Module:
    return cst.parse_module(code)


def cst_to_str(node) -> str:
    return cst.Module([]).code_for_node(node)


def format_code_str(code_snippet: str) -> str:
    return black.format_str(isort.code(code_snippet), mode=black.FileMode())


def get_name_change(item: str, changes: Dict[str, str]) -> str:
    if item in changes:
        return changes[item]
    return item


def remove_duplicate_calls(calls: list[str]) -> list:
    logger.debug({key: compress_logging_value(val) for key, val in locals().items()})
    return list(dict.fromkeys(calls))


def get_leading_comments(def_code: cst.FunctionDef) -> list:
    return [l for l in def_code.leading_lines if l.comment]


def is_not_private_and_has_leading_underscore(
    func_name: str, all_funcs: list[str], private_funcs: list[str]
) -> bool:
    logger.debug({key: compress_logging_value(val) for key, val in locals().items()})
    return (
        func_name.startswith("_")
        and func_name in all_funcs
        and func_name not in private_funcs
    )


def is_private_and_has_no_leading_underscore(
    func_name: str, all_funcs: list[str], private_funcs: list[str]
) -> bool:
    logger.debug({key: compress_logging_value(val) for key, val in locals().items()})
    return (
        not func_name.startswith("_")
        and func_name in all_funcs
        and func_name in private_funcs
    )


def strip_test_prefix_suffix(input_str: str) -> str:
    logger.debug({key: compress_logging_value(val) for key, val in locals().items()})
    return re.sub(r"(^test_|_test$)", "", input_str)

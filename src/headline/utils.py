import logging
import re
from typing import Dict

import libcst as cst

from ._logger import compress_logging_value

logger = logging.getLogger()


def strip_test_prefix_suffix(input_str: str) -> str:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    return re.sub(r"(^test_|_test$)", "", input_str)


def remove_duplicate_calls(calls: list) -> list:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    return list(dict.fromkeys(calls))


def is_not_private_and_has_leading_underscore(
    func_name: str, all_funcs: list, private_funcs: list
) -> bool:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    return (
        func_name.startswith("_")
        and func_name in all_funcs
        and func_name not in private_funcs
    )


def is_private_and_has_no_leading_underscore(
    func_name: str, all_funcs: list, private_funcs: list
) -> bool:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    return (
        not func_name.startswith("_")
        and func_name in all_funcs
        and func_name in private_funcs
    )


def get_func_name_edit(
    func_name: str, all_funcs: list, private_funcs: list
) -> str:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    if is_not_private_and_has_leading_underscore(
        func_name, all_funcs, private_funcs
    ):
        return func_name.lstrip("_")
    if is_private_and_has_no_leading_underscore(
        func_name, all_funcs, private_funcs
    ):
        return f"_{func_name}"
    return ""


def get_leading_lines(def_code: cst.FunctionDef, idx: int) -> list:
    for key, val in locals().items():
        logger.debug(f"{key} = {compress_logging_value(val)}")

    if idx == 0:
        return [cst.EmptyLine()] + get_leading_comments(def_code)
    return [] + get_leading_comments(def_code)


def get_leading_comments(def_code) -> list:
    return [l for l in def_code.leading_lines if l.comment]


def get_name_change(item: str, changes: Dict[str, str]) -> str:
    if item in changes:
        return changes[item]
    return item


def get_normed_test_key(item: str, is_test: bool) -> str:
    if is_test:
        return strip_test_prefix_suffix(item)
    return item

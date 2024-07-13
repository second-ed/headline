import re

import libcst as cst


def strip_test_prefix_suffix(input_str: str) -> str:
    return re.sub(r"(^test_|_test$)", "", input_str)


def remove_duplicate_calls(calls: list) -> list:
    return list(dict.fromkeys(calls))


def is_not_private_and_has_leading_underscore(
    func_name: str, all_funcs: list, private_funcs: list
) -> bool:
    return (
        func_name.startswith("_")
        and func_name in all_funcs
        and func_name not in private_funcs
    )


def is_private_and_has_no_leading_underscore(
    func_name: str, all_funcs: list, private_funcs: list
) -> bool:
    return (
        not func_name.startswith("_")
        and func_name in all_funcs
        and func_name in private_funcs
    )


def get_func_name_edit(
    func_name: str, all_funcs: list, private_funcs: list
) -> str:
    if is_not_private_and_has_leading_underscore(
        func_name, all_funcs, private_funcs
    ):
        return func_name.lstrip("_")
    if is_private_and_has_no_leading_underscore(
        func_name, all_funcs, private_funcs
    ):
        return f"_{func_name}"
    return ""


def get_leading_lines(idx: int) -> list:
    if idx == 0:
        return [cst.EmptyLine()]
    return []

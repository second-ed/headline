from contextlib import nullcontext as does_not_raise

import libcst as cst
import pytest
from headline.utils import (
    get_func_name_edit,
    get_leading_lines,
    is_not_private_and_has_leading_underscore,
    is_private_and_has_no_leading_underscore,
    remove_duplicate_calls,
    strip_test_prefix_suffix,
)


@pytest.mark.parametrize(
    "input_str, expected_result, expected_context",
    [
        ("test_case", "case", does_not_raise()),
        ("case_test", "case", does_not_raise()),
    ],
)
def test_strip_test_prefix_suffix(
    input_str, expected_result, expected_context
):
    with expected_context:
        assert strip_test_prefix_suffix(input_str) == expected_result


@pytest.mark.parametrize(
    "calls, expected_result, expected_context",
    [(["a", "a", "b", "a", "c"], ["a", "b", "c"], does_not_raise())],
)
def test_remove_duplicate_calls(calls, expected_result, expected_context):
    with expected_context:
        assert remove_duplicate_calls(calls) == expected_result


@pytest.mark.parametrize(
    "func_name, all_funcs, private_funcs, expected_result, expected_context",
    [
        ("_a", ["_a", "b", "c"], ["b"], True, does_not_raise()),
        ("_a", ["_a", "b", "c"], ["_a", "b"], False, does_not_raise()),
        ("_a", ["b", "c"], ["b"], False, does_not_raise()),
        ("a", ["a", "b", "c"], ["b"], False, does_not_raise()),
    ],
)
def test_is_not_private_and_has_leading_underscore(
    func_name, all_funcs, private_funcs, expected_result, expected_context
) -> None:
    with expected_context:
        assert (
            is_not_private_and_has_leading_underscore(
                func_name, all_funcs, private_funcs
            )
            == expected_result
        )


@pytest.mark.parametrize(
    "func_name, all_funcs, private_funcs, expected_result, expected_context",
    [
        ("a", ["a", "b", "c"], ["a"], True, does_not_raise()),
        ("_a", ["_a", "b", "c"], ["_a", "b"], False, does_not_raise()),
        ("_a", ["b", "c"], ["a", "b"], False, does_not_raise()),
        ("a", ["a", "b", "c"], ["b"], False, does_not_raise()),
    ],
)
def test_is_private_and_has_no_leading_underscore(
    func_name, all_funcs, private_funcs, expected_result, expected_context
) -> None:
    with expected_context:
        assert (
            is_private_and_has_no_leading_underscore(
                func_name, all_funcs, private_funcs
            )
            == expected_result
        )


@pytest.mark.parametrize(
    "func_name, all_funcs, private_funcs, expected_result, expected_context",
    [
        ("a", ["a", "b", "c"], ["a"], "_a", does_not_raise()),
        ("_a", ["_a", "b", "c"], ["_a", "b"], "", does_not_raise()),
        ("_a", ["_a", "b", "c"], ["b"], "a", does_not_raise()),
        ("a", ["a", "b", "c"], ["b"], "", does_not_raise()),
    ],
)
def test_get_func_name_edit(
    func_name, all_funcs, private_funcs, expected_result, expected_context
) -> None:
    with expected_context:
        assert (
            get_func_name_edit(func_name, all_funcs, private_funcs)
            == expected_result
        )


@pytest.mark.parametrize(
    "idx, expected_result, expected_context",
    [
        (-1, [], does_not_raise()),
        (
            0,
            [cst.EmptyLine()],
            does_not_raise(),
        ),
        (1, [], does_not_raise()),
    ],
)
def test_get_leading_lines(idx, expected_result, expected_context) -> None:
    with expected_context:
        res = get_leading_lines(idx)
        assert len(res) == len(expected_result)

        for res_line, exp_line in zip(res, expected_result):
            assert res_line.deep_equals(exp_line)

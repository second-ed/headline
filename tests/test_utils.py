from contextlib import nullcontext as does_not_raise

import libcst as cst
import pytest
from headline.utils import (
    get_func_name_edit,
    get_leading_lines,
    get_name_change,
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
    "fixture_name, idx, expected_result, expected_context",
    [
        ("get_func_def_no_comment", -1, [], does_not_raise()),
        (
            "get_func_def_no_comment",
            0,
            [cst.EmptyLine()],
            does_not_raise(),
        ),
        ("get_func_def_no_comment", 1, [], does_not_raise()),
        (
            "get_func_def_with_comment",
            -1,
            [
                cst.EmptyLine(
                    indent=True,
                    whitespace=cst.SimpleWhitespace(
                        value="",
                    ),
                    comment=cst.Comment(
                        value="#an expected comment",
                    ),
                    newline=cst.Newline(
                        value=None,
                    ),
                )
            ],
            does_not_raise(),
        ),
        (
            "get_func_def_with_comment",
            0,
            [
                cst.EmptyLine(),
                cst.EmptyLine(
                    indent=True,
                    whitespace=cst.SimpleWhitespace(
                        value="",
                    ),
                    comment=cst.Comment(
                        value="#an expected comment",
                    ),
                    newline=cst.Newline(
                        value=None,
                    ),
                ),
            ],
            does_not_raise(),
        ),
        (
            "get_func_def_with_comment",
            1,
            [
                cst.EmptyLine(
                    indent=True,
                    whitespace=cst.SimpleWhitespace(
                        value="",
                    ),
                    comment=cst.Comment(
                        value="#an expected comment",
                    ),
                    newline=cst.Newline(
                        value=None,
                    ),
                )
            ],
            does_not_raise(),
        ),
    ],
)
def test_get_leading_lines(
    request, fixture_name, idx, expected_result, expected_context
) -> None:
    with expected_context:
        def_code = request.getfixturevalue(fixture_name)
        res = get_leading_lines(def_code, idx)
        assert len(res) == len(expected_result)

        for res_line, exp_line in zip(res, expected_result):
            assert res_line.deep_equals(exp_line)


@pytest.mark.parametrize(
    "item, changes, expected_result, expected_context",
    [
        ("a", {"a": "_a", "b": "_b", "c": "_c"}, "_a", does_not_raise()),
        ("d", {"a": "_a", "b": "_b", "c": "_c"}, "d", does_not_raise()),
    ],
)
def test_get_name_change(item, changes, expected_result, expected_context):
    with expected_context:
        assert get_name_change(item, changes) == expected_result

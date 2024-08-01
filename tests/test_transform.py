import os
from contextlib import nullcontext as does_not_raise

import headline.sorters as st
import headline.transform as tf
import pytest
from headline import io
from headline._logger import get_dir_path


@pytest.mark.parametrize(
    "src_path, sorting_func, sorted_funcs, rename_funcs, expected_result_fixture_name, expected_name_changes_fixture_name, expected_context",
    [
        (
            get_dir_path(__file__, 0, "mock_package/src/utils_b.py"),
            st.sort_funcs_alphabetical,
            None,
            False,
            "get_fixture_utils_b_alphabetical",
            "get_transformer_no_name_changes",
            does_not_raise(),
        ),
        (
            get_dir_path(__file__, 0, "mock_package/src/utils_b.py"),
            st.sort_funcs_alphabetical_inc_leading_underscores,
            None,
            False,
            "get_fixture_utils_b_alphabetical_underscores",
            "get_transformer_no_name_changes",
            does_not_raise(),
        ),
        (
            get_dir_path(__file__, 0, "mock_package/src/utils_b.py"),
            st.sort_funcs_newspaper,
            None,
            False,
            "get_fixture_utils_b_newspaper",
            "get_transformer_no_name_changes",
            does_not_raise(),
        ),
        (
            get_dir_path(__file__, 0, "mock_package/src/utils_b.py"),
            st.sort_funcs_calls,
            None,
            False,
            "get_fixture_utils_b_calls",
            "get_transformer_no_name_changes",
            does_not_raise(),
        ),
        (
            get_dir_path(__file__, 0, "mock_package/src/utils_b.py"),
            st.sort_funcs_called,
            None,
            False,
            "get_fixture_utils_b_called",
            "get_transformer_no_name_changes",
            does_not_raise(),
        ),
        (
            get_dir_path(__file__, 0, "mock_package/src/utils_b.py"),
            None,
            ["d", "c", "e", "_b", "a"],
            False,
            "get_fixture_utils_b_manual",
            "get_transformer_no_name_changes",
            does_not_raise(),
        ),
        (
            get_dir_path(__file__, 0, "mock_package/src/utils_b.py"),
            st.sort_funcs_alphabetical,
            None,
            True,
            "get_fixture_utils_b_alphabetical_rename",
            "get_transformer_utils_b_name_changes",
            does_not_raise(),
        ),
        (
            get_dir_path(__file__, 0, "mock_package/src/utils_c.py"),
            st.sort_funcs_newspaper,
            None,
            True,
            "get_fixture_utils_c_newspaper_rename",
            "get_transformer_utils_c_name_changes",
            does_not_raise(),
        ),
        (
            get_dir_path(__file__, 0, "mock_package/src/utils_b.py"),
            None,
            None,
            False,
            "get_fixture_utils_b_manual",
            "get_transformer_no_name_changes",
            pytest.raises(ValueError),
        ),
    ],
)
def test_sort_src_funcs(
    request,
    src_path,
    sorting_func,
    sorted_funcs,
    rename_funcs,
    expected_result_fixture_name,
    expected_name_changes_fixture_name,
    expected_context,
):
    with expected_context:
        expected_code = request.getfixturevalue(expected_result_fixture_name)
        expected_name_changes = request.getfixturevalue(
            expected_name_changes_fixture_name
        )
        code, name_changes = tf.sort_src_funcs(
            src_path,
            sorting_func=sorting_func,
            sorted_funcs=sorted_funcs,
            rename_funcs=rename_funcs,
        )
        assert code == expected_code
        assert name_changes == expected_name_changes


@pytest.mark.parametrize(
    "test_path, src_code_fixture_name, call_name_change, expected_result_fixture_name, expected_context",
    [
        (
            get_dir_path(__file__, 0, "mock_package/tests/test_utils_a.py"),
            "get_fixture_utils_a_calls_rename",
            {"add": "_add", "_subtract": "subtract", "multiply": "_multiply"},
            "get_fixture_test_utils_a_calls_rename",
            does_not_raise(),
        ),
        (
            get_dir_path(__file__, 0, "mock_package/tests/test_utils_b.py"),
            "get_fixture_utils_b_newspaper_rename",
            {"a": "_a"},
            "get_fixture_test_utils_b_newspaper_rename",
            does_not_raise(),
        ),
    ],
)
def test_sort_test_funcs(
    request,
    test_path,
    src_code_fixture_name,
    call_name_change,
    expected_result_fixture_name,
    expected_context,
):
    with expected_context:
        src_code = request.getfixturevalue(src_code_fixture_name)
        expected_result = request.getfixturevalue(expected_result_fixture_name)
        assert (
            tf.sort_test_funcs(test_path, src_code, call_name_change)
            == expected_result
        )


@pytest.mark.parametrize(
    "src_path, test_path, inp_sort_type, inp_tests_only, inp_rename, expected_src_result_fixture_name, expected_test_result_fixture_name, expected_context",
    [
        (
            get_dir_path(__file__, 0, "mock_package/src/utils_b.py"),
            get_dir_path(__file__, 0, "mock_package/tests/test_utils_b.py"),
            "newspaper",
            False,
            True,
            "get_fixture_utils_b_newspaper_rename",
            "get_fixture_test_utils_b_newspaper_rename",
            does_not_raise(),
        )
    ],
)
def test_sort_src_funcs_and_tests(
    request,
    src_path,
    test_path,
    inp_sort_type,
    inp_tests_only,
    inp_rename,
    expected_src_result_fixture_name,
    expected_test_result_fixture_name,
    expected_context,
):
    with expected_context:
        expected_src_result = request.getfixturevalue(
            expected_src_result_fixture_name
        )
        expected_test_result = request.getfixturevalue(
            expected_test_result_fixture_name
        )

        tf.sort_src_funcs_and_tests(
            src_path,
            test_path,
            inp_sort_type,
            inp_tests_only,
            inp_rename,
            "test",
        )

        created_src_path = src_path.replace(".py", "_test.py")
        created_test_path = test_path.replace(".py", "_test.py")

        actual_src_result = io.get_src_code(created_src_path)
        actual_test_result = io.get_src_code(created_test_path)

        try:
            assert actual_src_result == expected_src_result
            assert actual_test_result == expected_test_result
        finally:
            # clean up after myself
            os.remove(created_src_path)
            os.remove(created_test_path)

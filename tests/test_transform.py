from contextlib import nullcontext as does_not_raise

import headline.sorters as st
import headline.transform as tf
import pytest
from headline._logger import get_dir_path


@pytest.mark.parametrize(
    "src_path, sorting_func, rename_funcs, expected_result_fixture_name, expected_context",
    [
        (
            get_dir_path(__file__, 0, "mock_package/src/utils_b.py"),
            st.sort_funcs_alphabetical,
            False,
            "get_utils_b_alphabetical_sorted",
            does_not_raise(),
        ),
        (
            get_dir_path(__file__, 0, "mock_package/src/utils_b.py"),
            st.sort_funcs_alphabetical_inc_leading_underscores,
            False,
            "get_utils_b_alphabetical_inc_leading_underscores_sorted",
            does_not_raise(),
        ),
        (
            get_dir_path(__file__, 0, "mock_package/src/utils_b.py"),
            st.sort_funcs_newspaper,
            False,
            "get_utils_b_newspaper_sorted",
            does_not_raise(),
        ),
        (
            get_dir_path(__file__, 0, "mock_package/src/utils_b.py"),
            st.sort_funcs_calls,
            False,
            "get_utils_b_calls_sorted",
            does_not_raise(),
        ),
        (
            get_dir_path(__file__, 0, "mock_package/src/utils_b.py"),
            st.sort_funcs_called,
            False,
            "get_utils_b_called_sorted",
            does_not_raise(),
        ),
    ],
)
def test_sort_src_funcs(
    request,
    src_path,
    sorting_func,
    rename_funcs,
    expected_result_fixture_name,
    expected_context,
):
    with expected_context:
        expected_result = request.getfixturevalue(expected_result_fixture_name)
        assert (
            tf.sort_src_funcs(
                src_path, sorting_func=sorting_func, rename_funcs=rename_funcs
            )
            == expected_result
        )

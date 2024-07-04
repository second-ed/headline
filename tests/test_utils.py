from contextlib import nullcontext as does_not_raise

import pytest
from headline.utils import remove_duplicate_calls


@pytest.mark.parametrize(
    "calls, expected_result, expected_context",
    [(["a", "a", "b", "a", "c"], ["a", "b", "c"], does_not_raise())],
)
def test_remove_duplicate_calls(calls, expected_result, expected_context):
    with expected_context:
        assert remove_duplicate_calls(calls) == expected_result

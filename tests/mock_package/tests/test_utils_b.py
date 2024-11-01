from contextlib import nullcontext as does_not_raise

import pytest

from tests.mock_package.src import utils_b as ub


@pytest.mark.parametrize(
    "expected_result, expected_context",
    [
        (1, does_not_raise()),
    ],
)
def test_a(expected_result, expected_context):
    with expected_context:
        assert ub.a() == expected_result


@pytest.mark.parametrize(
    "expected_result, expected_context",
    [
        (0, does_not_raise()),
    ],
)
def test_b(expected_result, expected_context):
    with expected_context:
        assert ub._b() == expected_result


@pytest.mark.parametrize(
    "expected_context",
    [
        (does_not_raise()),
    ],
)
def test_c(expected_context):
    with expected_context:
        # This function does not return anything, we just ensure it runs without error
        assert ub.c() is None


@pytest.mark.parametrize(
    "expected_result, expected_context",
    [
        (1, does_not_raise()),
    ],
)
def test_d(expected_result, expected_context):
    with expected_context:
        assert ub.d() == expected_result


@pytest.mark.parametrize(
    "expected_context",
    [
        (does_not_raise()),
    ],
)
def test_e(expected_context):
    with expected_context:
        # This function does not return anything, we just ensure it runs without error
        assert ub.e() is None

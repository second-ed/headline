from contextlib import nullcontext as does_not_raise

import pytest

from tests.mock_package.src.utils_a import (
    _subtract,
    add,
    divide,
    factorial,
    fibonacci,
    is_prime,
    multiply,
    power,
)

@pytest.mark.parametrize(
    "a, b, expected_result, expected_context",
    [
        (5, 2, 7, does_not_raise()),
    ],
)
def test_add(a, b, expected_result, expected_context):
    with expected_context:
        assert add(a, b) == expected_result


@pytest.mark.parametrize(
    "a, b, expected_result, expected_context",
    [
        (10, 2, 20, does_not_raise()),
    ],
)
def test_multiply(a, b, expected_result, expected_context):
    with expected_context:
        assert multiply(a, b) == expected_result


@pytest.mark.parametrize(
    "a, b, expected_result, expected_context",
    [
        (6, 3, 2, does_not_raise()),
        (5, 2, 2.5, does_not_raise()),
        (1, 0, None, pytest.raises(ValueError, match="Cannot divide by zero")),
    ],
)
def test_divide(a, b, expected_result, expected_context):
    with expected_context:
        assert divide(a, b) == expected_result


@pytest.mark.parametrize(
    "n, expected_result, expected_context",
    [
        (0, 1, does_not_raise()),
        (1, 1, does_not_raise()),
        (5, 120, does_not_raise()),
        (
            -1,
            None,
            pytest.raises(
                ValueError,
            ),
        ),
    ],
)
def test_factorial(n, expected_result, expected_context):
    with expected_context:
        assert factorial(n) == expected_result


@pytest.mark.parametrize(
    "n, expected_result, expected_context",
    [
        (0, 0, does_not_raise()),
        (1, 1, does_not_raise()),
        (10, 55, does_not_raise()),
        (
            -1,
            None,
            pytest.raises(
                ValueError,
            ),
        ),
    ],
)
def test_fibonacci(n, expected_result, expected_context):
    with expected_context:
        assert fibonacci(n) == expected_result


@pytest.mark.parametrize(
    "n, expected_result, expected_context",
    [
        (4, False, does_not_raise()),
        (6, False, does_not_raise()),
        (7, True, does_not_raise()),
        (-1, False, does_not_raise()),
    ],
)
def test_is_prime(n, expected_result, expected_context):
    with expected_context:
        assert is_prime(n) == expected_result


@pytest.mark.parametrize(
    "base, exponent, expected_result, expected_context",
    [
        (2, 3, 8, does_not_raise()),
        (5, 0, 1, does_not_raise()),
        (
            2,
            -1,
            None,
            pytest.raises(ValueError),
        ),
    ],
)
def test_power(base, exponent, expected_result, expected_context):
    with expected_context:
        assert power(base, exponent) == expected_result


@pytest.mark.parametrize(
    "a, b, expected_result, expected_context",
    [
        (5, 2, 3, does_not_raise()),
        (2, 2, 0, does_not_raise()),
        (0, 5, -5, does_not_raise()),
    ],
)
def test_subtract(a, b, expected_result, expected_context):
    with expected_context:
        assert _subtract(a, b) == expected_result



from typing import List

import libcst as cst
import pytest
from headline._logger import get_dir_path
from headline.transform import _get_src_module, _get_visitor


@pytest.fixture
def get_transformer_no_name_changes():
    return {}


@pytest.fixture
def get_transformer_utils_b_name_changes():
    return {"a": "_a"}


@pytest.fixture
def get_transformer_utils_c_name_changes():
    return {
        "check_extension": "_check_extension",
        "clean_data": "_clean_data",
        "filepath_exists": "_filepath_exists",
        "merge_data": "_merge_data",
        "read_data": "_read_data",
        "rename_data": "_rename_data",
        "replacer": "_replacer",
        "save_data": "_save_data",
        "transform": "_transform",
    }


@pytest.fixture
def get_func_no_comment():
    return "def test():\n    pass\n"


@pytest.fixture
def get_func_def_no_comment(get_func_no_comment):
    return cst.parse_statement(get_func_no_comment)


@pytest.fixture
def get_func_with_comment():
    return "#an expected comment\ndef test():\n    pass\n"


@pytest.fixture
def get_func_def_with_comment(get_func_with_comment):
    return cst.parse_statement(get_func_with_comment)


@pytest.fixture
def get_utils_a_default() -> str:
    return (
        "\n"
        "def factorial(n):\n"
        "    if n < 0:\n"
        '        raise ValueError("Factorial is not defined for negative numbers")\n'
        "    if n == 0 or n == 1:\n"
        "        return 1\n"
        "    result = 1\n"
        "    for i in range(2, n + 1):\n"
        "        result = _multiply(result, i)\n"
        "    return result\n"
        "\n"
        "\n"
        "def fibonacci(n):\n"
        "    if n < 0:\n"
        '        raise ValueError("Fibonacci is not defined for negative numbers")\n'
        "    if n == 0:\n"
        "        return 0\n"
        "    if n == 1:\n"
        "        return 1\n"
        "    a, b = 0, 1\n"
        "    for _ in range(2, n + 1):\n"
        "        a, b = b, _add(a, b)\n"
        "    return b\n"
        "\n"
        "\n"
        "def power(base, exponent):\n"
        "    if exponent < 0:\n"
        '        raise ValueError("Exponent should be non-negative")\n'
        "    result = 1\n"
        "    for _ in range(exponent):\n"
        "        result = _multiply(result, base)\n"
        "    return result\n"
        "\n"
        "\n"
        "def divide(a, b):\n"
        "    if b == 0:\n"
        '        raise ValueError("Cannot divide by zero")\n'
        "    return a / b\n"
        "\n"
        "\n"
        "def is_prime(n):\n"
        "    if n <= 1:\n"
        "        return False\n"
        "    if n <= 3:\n"
        "        return True\n"
        "    if n % 2 == 0 or n % 3 == 0:\n"
        "        return False\n"
        "    i = 5\n"
        "    while i * i <= n:\n"
        "        if n % i == 0 or n % (i + 2) == 0:\n"
        "            return False\n"
        "        i += 6\n"
        "    return True\n"
        "\n"
        "\n"
        "def subtract(a, b):\n"
        "    return a - b\n"
        "\n"
        "\n"
        "def _multiply(a, b):\n"
        "    res = 0\n"
        "    for _ in range(b):\n"
        "        res = _add(res, a)\n"
        "\n"
        "    return res\n"
        "\n"
        "\n"
        "def _add(a, b):\n"
        "    return a + b\n"
        "\n"
        "\n"
        ""
    )


@pytest.fixture
def get_test_utils_a_default() -> str:
    return (
        "from contextlib import nullcontext as does_not_raise\n"
        "\n"
        "import pytest\n"
        "\n"
        "from tests.mock_package.src.utils_a import (\n"
        "    subtract,\n"
        "    _add,\n"
        "    divide,\n"
        "    factorial,\n"
        "    fibonacci,\n"
        "    is_prime,\n"
        "    _multiply,\n"
        "    power,\n"
        ")\n"
        "\n"
        "@pytest.mark.parametrize(\n"
        '    "n, expected_result, expected_context",\n'
        "    [\n"
        "        (0, 1, does_not_raise()),\n"
        "        (1, 1, does_not_raise()),\n"
        "        (5, 120, does_not_raise()),\n"
        "        (\n"
        "            -1,\n"
        "            None,\n"
        "            pytest.raises(\n"
        "                ValueError,\n"
        "            ),\n"
        "        ),\n"
        "    ],\n"
        ")\n"
        "def test_factorial(n, expected_result, expected_context):\n"
        "    with expected_context:\n"
        "        assert factorial(n) == expected_result\n"
        "\n"
        "\n"
        "@pytest.mark.parametrize(\n"
        '    "n, expected_result, expected_context",\n'
        "    [\n"
        "        (0, 0, does_not_raise()),\n"
        "        (1, 1, does_not_raise()),\n"
        "        (10, 55, does_not_raise()),\n"
        "        (\n"
        "            -1,\n"
        "            None,\n"
        "            pytest.raises(\n"
        "                ValueError,\n"
        "            ),\n"
        "        ),\n"
        "    ],\n"
        ")\n"
        "def test_fibonacci(n, expected_result, expected_context):\n"
        "    with expected_context:\n"
        "        assert fibonacci(n) == expected_result\n"
        "\n"
        "\n"
        "@pytest.mark.parametrize(\n"
        '    "base, exponent, expected_result, expected_context",\n'
        "    [\n"
        "        (2, 3, 8, does_not_raise()),\n"
        "        (5, 0, 1, does_not_raise()),\n"
        "        (\n"
        "            2,\n"
        "            -1,\n"
        "            None,\n"
        "            pytest.raises(ValueError),\n"
        "        ),\n"
        "    ],\n"
        ")\n"
        "def test_power(base, exponent, expected_result, expected_context):\n"
        "    with expected_context:\n"
        "        assert power(base, exponent) == expected_result\n"
        "\n"
        "\n"
        "@pytest.mark.parametrize(\n"
        '    "a, b, expected_result, expected_context",\n'
        "    [\n"
        "        (6, 3, 2, does_not_raise()),\n"
        "        (5, 2, 2.5, does_not_raise()),\n"
        '        (1, 0, None, pytest.raises(ValueError, match="Cannot divide by zero")),\n'
        "    ],\n"
        ")\n"
        "def test_divide(a, b, expected_result, expected_context):\n"
        "    with expected_context:\n"
        "        assert divide(a, b) == expected_result\n"
        "\n"
        "\n"
        "@pytest.mark.parametrize(\n"
        '    "n, expected_result, expected_context",\n'
        "    [\n"
        "        (4, False, does_not_raise()),\n"
        "        (6, False, does_not_raise()),\n"
        "        (7, True, does_not_raise()),\n"
        "        (-1, False, does_not_raise()),\n"
        "    ],\n"
        ")\n"
        "def test_is_prime(n, expected_result, expected_context):\n"
        "    with expected_context:\n"
        "        assert is_prime(n) == expected_result\n"
        "\n"
        "\n"
        "@pytest.mark.parametrize(\n"
        '    "a, b, expected_result, expected_context",\n'
        "    [\n"
        "        (5, 2, 3, does_not_raise()),\n"
        "        (2, 2, 0, does_not_raise()),\n"
        "        (0, 5, -5, does_not_raise()),\n"
        "    ],\n"
        ")\n"
        "def test_subtract(a, b, expected_result, expected_context):\n"
        "    with expected_context:\n"
        "        assert subtract(a, b) == expected_result\n"
        "\n"
        "\n"
        "@pytest.mark.parametrize(\n"
        '    "a, b, expected_result, expected_context",\n'
        "    [\n"
        "        (10, 2, 20, does_not_raise()),\n"
        "    ],\n"
        ")\n"
        "def test_multiply(a, b, expected_result, expected_context):\n"
        "    with expected_context:\n"
        "        assert _multiply(a, b) == expected_result\n"
        "\n"
        "\n"
        "@pytest.mark.parametrize(\n"
        '    "a, b, expected_result, expected_context",\n'
        "    [\n"
        "        (5, 2, 7, does_not_raise()),\n"
        "    ],\n"
        ")\n"
        "def test_add(a, b, expected_result, expected_context):\n"
        "    with expected_context:\n"
        "        assert _add(a, b) == expected_result\n"
        "\n"
        "\n"
        ""
    )


@pytest.fixture
def get_utils_b_alphabetical_sorted() -> str:
    return (
        "\ndef a():\n"
        "    return 1\n\n\n"
        "def _b():\n"
        "    return 0\n\n\n"
        "def c():\n"
        "    a()\n\n\n"
        "def d():\n"
        "    res = a() + _b()\n"
        "    return res\n\n\n"
        "def e():\n"
        "    _b()\n\n\n"
    )


@pytest.fixture
def get_utils_b_alphabetical_inc_leading_underscores_sorted() -> str:
    return (
        "\ndef _b():\n"
        "    return 0\n\n\n"
        "def a():\n"
        "    return 1\n\n\n"
        "def c():\n"
        "    a()\n\n\n"
        "def d():\n"
        "    res = a() + _b()\n"
        "    return res\n\n\n"
        "def e():\n"
        "    _b()\n\n\n"
    )


@pytest.fixture
def get_utils_b_newspaper_sorted() -> str:
    return (
        "\ndef d():\n"
        "    res = a() + _b()\n"
        "    return res\n\n\n"
        "def c():\n"
        "    a()\n\n\n"
        "def e():\n"
        "    _b()\n\n\n"
        "def a():\n"
        "    return 1\n\n\n"
        "def _b():\n"
        "    return 0\n\n\n"
    )


@pytest.fixture
def get_utils_b_calls_sorted() -> str:
    return (
        "\ndef d():\n"
        "    res = a() + _b()\n"
        "    return res\n\n\n"
        "def c():\n"
        "    a()\n\n\n"
        "def e():\n"
        "    _b()\n\n\n"
        "def a():\n"
        "    return 1\n\n\n"
        "def _b():\n"
        "    return 0\n\n\n"
    )


@pytest.fixture
def get_utils_b_called_sorted() -> str:
    return (
        "\ndef a():\n"
        "    return 1\n\n\n"
        "def _b():\n"
        "    return 0\n\n\n"
        "def c():\n"
        "    a()\n\n\n"
        "def d():\n"
        "    res = a() + _b()\n"
        "    return res\n\n\n"
        "def e():\n    _b()\n\n\n"
    )


@pytest.fixture
def get_utils_b_manual_sorted() -> str:
    return (
        "\ndef d():\n"
        "    res = a() + _b()\n"
        "    return res\n\n\n"
        "def c():\n"
        "    a()\n\n\n"
        "def e():\n"
        "    _b()\n\n\n"
        "def _b():\n"
        "    return 0\n\n\n"
        "def a():\n"
        "    return 1\n\n\n"
    )


@pytest.fixture
def get_utils_b_alphabetical_rename() -> str:
    return (
        "\ndef _a():\n"
        "    return 1\n\n\n"
        "def _b():\n"
        "    return 0\n\n\n"
        "def c():\n"
        "    _a()\n\n\n"
        "def d():\n"
        "    res = _a() + _b()\n"
        "    return res\n\n\n"
        "def e():\n"
        "    _b()\n\n\n"
    )


@pytest.fixture
def get_utils_b_newspaper_rename() -> str:
    return (
        "\ndef d():\n"
        "    res = _a() + _b()\n"
        "    return res\n\n\n"
        "def c():\n"
        "    _a()\n\n\n"
        "def e():\n"
        "    _b()\n\n\n"
        "def _a():\n"
        "    return 1\n\n\n"
        "def _b():\n"
        "    return 0\n\n\n"
    )


@pytest.fixture
def get_test_utils_b_newspaper() -> str:
    return (
        "from contextlib import nullcontext as does_not_raise\n\n"
        "import pytest\n\n"
        "from tests.mock_package.src import utils_b as ub\n\n"
        '@pytest.mark.parametrize(\n    "expected_result, expected_context",\n'
        "    [\n        (1, does_not_raise()),\n    ],\n)\n"
        "def test_d(expected_result, expected_context):\n"
        "    with expected_context:\n"
        "        assert ub.d() == expected_result\n\n\n"
        '@pytest.mark.parametrize(\n    "expected_context",\n'
        "    [\n        (does_not_raise()),\n    ],\n)\n"
        "def test_c(expected_context):\n    with expected_context:\n"
        "        # This function does not return anything, we just ensure it runs without error\n"
        "        assert ub.c() is None\n\n\n@pytest.mark.parametrize(\n"
        '    "expected_context",\n    [\n        (does_not_raise()),\n'
        "    ],\n)\ndef test_e(expected_context):\n    with expected_context:\n"
        "        # This function does not return anything, we just ensure it runs without error\n"
        "        assert ub.e() is None\n\n\n@pytest.mark.parametrize(\n"
        '    "expected_result, expected_context",\n    [\n'
        "        (1, does_not_raise()),\n    ],\n)\n"
        "def test_a(expected_result, expected_context):\n"
        "    with expected_context:\n        assert ub._a() == expected_result\n\n\n"
        '@pytest.mark.parametrize(\n    "expected_result, expected_context",\n    [\n'
        "        (0, does_not_raise()),\n    ],\n)\n"
        "def test_b(expected_result, expected_context):\n"
        "    with expected_context:\n"
        "        assert ub._b() == expected_result\n\n\n"
    )


@pytest.fixture
def get_utils_c_newspaper_rename() -> str:
    return (
        '"""module level description"""\n\n'
        "import re\n\n"
        "import pandas as pd\n\n"
        "def main(filepath: str) -> bool:\n"
        "    data = _read_data(filepath)\n"
        "    data = _clean_data(data)\n"
        "    data_dict = _transform_data(data)\n\n"
        "    for key, value in data_dict.items():\n"
        "        data_dict[key] = _rename_data(value)\n\n"
        "    merged_data = _merge_data(data_dict)\n\n"
        "    return _save_data(merged_data, filepath)\n\n\n"
        "# this is a comment related to the function below\n"
        "def _read_data(filepath: str) -> pd.DataFrame:\n"
        "    if _check_extension(filepath):\n"
        "        return pd.DataFrame({})\n"
        "    raise FileNotFoundError\n\n\n"
        "def _save_data(data: pd.DataFrame, filepath: str) -> bool:\n"
        "    if _filepath_exists(filepath):\n"
        "        return True\n"
        "    return False\n\n\n"
        "def _check_extension(filepath: str):\n"
        '    """this is a docstring\n\n'
        "    Args:\n"
        "        filepath (str): the filepath to check\n\n"
        "    Returns:\n"
        '        bool: if the extension is valid\n    """\n'
        "    return True\n\n\n"
        "def _clean_data(data: pd.DataFrame) -> pd.DataFrame:\n"
        "    return data\n\n\ndef _filepath_exists(filepath: str):\n"
        "    return True\n\n\n"
        "def _merge_data(data_dict):\n"
        "    # this is an inline comment that hopefully will stay\n"
        "    data = pd.concat([v for v in data_dict.values()])\n"
        "    return data\n\n\n"
        "def _rename_data(value):\n"
        "    def _replacer(match):\n"
        "        content = match.group(1)\n"
        '        cleaned_content = " ".join(content.split())\n'
        '        return f"({cleaned_content})"\n\n'
        '    return re.sub(r"\\((.*?)\\)", _replacer, value, flags=re.DOTALL)\n\n\n'
        "def _transform_data(data):\n"
        "    def _transform():\n"
        "        return data\n\n"
        "    return _transform()\n\n\n"
    )


@pytest.fixture
def get_mock_package_all_files() -> List[str]:
    return [
        "some_package/src/__init__.py",
        "some_package/src/utils_a.py",
        "some_package/src/utils_b.py",
        "some_package/src/utils_c.py",
        "some_package/tests/__init__.py",
        "some_package/tests/test_utils_a.py",
        "some_package/tests/test_utils_b.py",
    ]


@pytest.fixture
def get_utils_a_visitor():
    fv = _get_visitor(
        _get_src_module(
            get_dir_path(__file__, 0, "mock_package/src/utils_a.py")
        )
    )
    fv.process_func_defs()
    return fv


@pytest.fixture
def get_utils_a_visitor_expected_attrs():
    return {
        "imports": {},
        "func_def_keys": [
            "add",
            "_subtract",
            "multiply",
            "divide",
            "power",
            "factorial",
            "fibonacci",
            "is_prime",
        ],
        "top_level_funcs": [
            "add",
            "_subtract",
            "multiply",
            "divide",
            "power",
            "factorial",
            "fibonacci",
            "is_prime",
        ],
        # "calls": {
        #     "multiply": ["range", "add"],
        #     "divide": ["ValueError"],
        #     "power": ["ValueError", "range", "multiply"],
        #     "factorial": ["ValueError", "range", "multiply"],
        #     "fibonacci": ["ValueError", "range", "add"],
        #     "add": [],
        #     "_subtract": [],
        #     "is_prime": [],
        # },
        # "called_by": {
        #     "range": ["multiply", "power", "factorial", "fibonacci"],
        #     "add": ["multiply", "fibonacci"],
        #     "ValueError": ["divide", "power", "factorial", "fibonacci"],
        #     "multiply": ["power", "factorial"],
        #     "_subtract": [],
        #     "divide": [],
        #     "power": [],
        #     "factorial": [],
        #     "fibonacci": [],
        #     "is_prime": [],
        # },
    }


@pytest.fixture
def get_test_utils_a_visitor():
    fv = _get_visitor(
        _get_src_module(
            get_dir_path(__file__, 0, "mock_package/tests/test_utils_a.py")
        )
    )
    fv.process_func_defs()
    return fv


@pytest.fixture
def get_test_utils_a_visitor_expected_attrs():
    return {
        "imports": {
            "contextlib": {"name": "nullcontext", "as_name": "does_not_raise"},
            "pytest": {"name": "pytest", "as_name": "pytest"},
            "tests.mock_package.src.utils_a": {
                "name": "power",
                "as_name": "power",
            },
        },
        "func_def_keys": [
            "test_multiply",
            "test_add",
            "test_subtract",
            "test_divide",
            "test_power",
            "test_factorial",
            "test_fibonacci",
            "test_is_prime",
        ],
        "top_level_funcs": [
            "test_multiply",
            "test_add",
            "test_subtract",
            "test_divide",
            "test_power",
            "test_factorial",
            "test_fibonacci",
            "test_is_prime",
        ],
    }

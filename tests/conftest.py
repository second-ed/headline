from typing import List

import pytest


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

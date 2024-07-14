import pytest


@pytest.fixture
def get_utils_b_alphabetical_sorted():
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
def get_utils_b_alphabetical_inc_leading_underscores_sorted():
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
def get_utils_b_newspaper_sorted():
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
def get_utils_b_calls_sorted():
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
def get_utils_b_called_sorted():
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
def get_utils_b_manual_sorted():
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
def get_mock_package_all_files():
    return [
        "some_package/src/__init__.py",
        "some_package/src/utils_a.py",
        "some_package/src/utils_b.py",
        "some_package/src/utils_c.py",
        "some_package/tests/__init__.py",
        "some_package/tests/test_utils_a.py",
        "some_package/tests/test_utils_b.py",
    ]

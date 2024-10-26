import os
import shutil

import headline.io as io
import headline.process as proc
import pytest
from headline._logger import get_dir_path
from headline.utils import format_code_str


def create_mock_package():
    src_files = {
        "mock_data/utils_a_alphabetical.py": "utils_a.py",
        "mock_data/utils_b_calls.py": "utils_b.py",
        "mock_data/utils_c_called.py": "utils_c.py",
    }
    test_files = {
        "mock_data/test_utils_a_alphabetical_underscores.py": "test_utils_a.py",
        "mock_data/test_utils_b_newspaper.py": "test_utils_b.py",
    }

    mock_root = get_dir_path(__file__, 1)
    mock_src_path = os.path.join(
        mock_root, "inplace_mock_package/src/mock_package"
    )
    mock_tests_path = os.path.join(mock_root, "inplace_mock_package/tests")

    for path in [mock_src_path, mock_tests_path]:
        os.makedirs(path, exist_ok=True)
        io.save_modified_code("", f"{path}/__init__.py")

    for k, v in src_files.items():
        path = os.path.join(mock_root, k)
        code = io.get_src_code(path)
        io.save_modified_code(code, f"{mock_src_path}/{v}")

    for k, v in test_files.items():
        path = os.path.join(mock_root, k)
        code = io.get_src_code(path)
        io.save_modified_code(code, f"{mock_tests_path}/{v}")


@pytest.mark.parametrize(
    "sort_type, rename",
    [
        ("newspaper", "_rename"),
        ("newspaper", ""),  # empty string = no rename
        ("calls", "_rename"),
        ("called", ""),
        ("alphabetical", "_rename"),
    ],
)
def test_main_process(request, sort_type, rename):
    create_mock_package()

    mock_root = f"{get_dir_path(__file__, 1)}/inplace_mock_package/"

    proc.main_process(
        mock_root,
        "src",
        "tests",
        sort_type,
        False,
        bool(rename),
        "",
    )

    actual_utils_a = io.get_src_code(f"{mock_root}src/mock_package/utils_a.py")

    expected_utils_a = request.getfixturevalue(
        f"get_fixture_utils_a_{sort_type}{rename}"
    )

    actual_test_utils_a = io.get_src_code(f"{mock_root}tests/test_utils_a.py")

    expected_test_utils_a = request.getfixturevalue(
        f"get_fixture_test_utils_a_{sort_type}{rename}"
    )

    actual_utils_b = io.get_src_code(f"{mock_root}src/mock_package/utils_b.py")

    expected_utils_b = request.getfixturevalue(
        f"get_fixture_utils_b_{sort_type}{rename}"
    )
    actual_test_utils_b = io.get_src_code(f"{mock_root}tests/test_utils_b.py")

    expected_test_utils_b = request.getfixturevalue(
        f"get_fixture_test_utils_b_{sort_type}{rename}"
    )

    actual_utils_c = io.get_src_code(f"{mock_root}src/mock_package/utils_c.py")

    expected_utils_c = request.getfixturevalue(
        f"get_fixture_utils_c_{sort_type}{rename}"
    )

    try:
        assert format_code_str(actual_utils_a) == format_code_str(
            expected_utils_a
        )
        assert format_code_str(actual_test_utils_a) == format_code_str(
            expected_test_utils_a
        )
        assert format_code_str(actual_utils_b) == format_code_str(
            expected_utils_b
        )
        assert format_code_str(actual_test_utils_b) == format_code_str(
            expected_test_utils_b
        )
        assert format_code_str(actual_utils_c) == format_code_str(
            expected_utils_c
        )

    finally:
        # cleanup
        shutil.rmtree(mock_root)

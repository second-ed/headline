import os
import shutil

import headline.io as io
import headline.process as proc
from headline._logger import get_dir_path


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

    mock_base_path = get_dir_path(__file__, 1)
    mock_src_path = os.path.join(
        mock_base_path, "inplace_mock_package/src/mock_package"
    )
    mock_tests_path = os.path.join(
        mock_base_path, "inplace_mock_package/tests"
    )

    for path in [mock_src_path, mock_tests_path]:
        os.makedirs(path, exist_ok=True)
        io.save_modified_code("", f"{path}/__init__.py")

    for k, v in src_files.items():
        path = os.path.join(mock_base_path, k)
        code = io.get_src_code(path)
        io.save_modified_code(code, f"{mock_src_path}/{v}")

    for k, v in test_files.items():
        path = os.path.join(mock_base_path, k)
        code = io.get_src_code(path)
        io.save_modified_code(code, f"{mock_tests_path}/{v}")


def test_main_process(request):
    create_mock_package()

    proc.main_process(
        f"{get_dir_path(__file__, 1)}/inplace_mock_package/",
        "src",
        "tests",
        "newspaper",
        False,
        False,
        "",
    )

    actual_utils_a = io.get_src_code(
        f"{get_dir_path(__file__, 1)}/inplace_mock_package/src/mock_package/utils_a.py"
    ).strip("\n")

    expected_utils_a = request.getfixturevalue(
        "get_fixture_utils_a_newspaper"
    ).strip("\n")

    actual_test_utils_a = io.get_src_code(
        f"{get_dir_path(__file__, 1)}/inplace_mock_package/tests/test_utils_a.py"
    ).strip("\n")

    expected_test_utils_a = request.getfixturevalue(
        "get_fixture_test_utils_a_newspaper"
    ).strip("\n")

    actual_utils_b = io.get_src_code(
        f"{get_dir_path(__file__, 1)}/inplace_mock_package/src/mock_package/utils_b.py"
    ).strip("\n")

    expected_utils_b = request.getfixturevalue(
        "get_fixture_utils_b_newspaper"
    ).strip("\n")

    actual_test_utils_b = io.get_src_code(
        f"{get_dir_path(__file__, 1)}/inplace_mock_package/tests/test_utils_b.py"
    ).strip("\n")

    expected_test_utils_b = request.getfixturevalue(
        "get_fixture_test_utils_b_newspaper"
    ).strip("\n")

    actual_utils_c = io.get_src_code(
        f"{get_dir_path(__file__, 1)}/inplace_mock_package/src/mock_package/utils_c.py"
    ).strip("\n")

    expected_utils_c = request.getfixturevalue(
        "get_fixture_utils_c_newspaper"
    ).strip("\n")

    assert actual_utils_a == expected_utils_a
    assert actual_test_utils_a == expected_test_utils_a
    assert actual_utils_b == expected_utils_b
    assert actual_test_utils_b == expected_test_utils_b
    assert actual_utils_c == expected_utils_c

    # cleanup
    shutil.rmtree(f"{get_dir_path(__file__, 1)}/inplace_mock_package")

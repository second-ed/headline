from contextlib import nullcontext as does_not_raise

import pytest
from headline import io
from headline._logger import get_dir_path


@pytest.mark.parametrize(
    "search_folders, expected_result, expected_context",
    [
        (
            ["src"],
            [
                "some_package/src/__init__.py",
                "some_package/src/utils_a.py",
                "some_package/src/utils_b.py",
                "some_package/src/utils_c.py",
            ],
            does_not_raise(),
        ),
        (
            ["tests"],
            [
                "some_package/tests/__init__.py",
                "some_package/tests/test_utils_a.py",
                "some_package/tests/test_utils_b.py",
            ],
            does_not_raise(),
        ),
        (
            ["src", "tests"],
            [
                "some_package/src/__init__.py",
                "some_package/src/utils_a.py",
                "some_package/src/utils_b.py",
                "some_package/src/utils_c.py",
                "some_package/tests/__init__.py",
                "some_package/tests/test_utils_a.py",
                "some_package/tests/test_utils_b.py",
            ],
            does_not_raise(),
        ),
    ],
)
def test_find_files_in_folders(
    get_mock_package_all_files,
    search_folders,
    expected_result,
    expected_context,
) -> None:
    with expected_context:
        assert (
            io.find_files_in_folders(
                get_mock_package_all_files, search_folders
            )
            == expected_result
        )


@pytest.mark.parametrize(
    "src_files, test_files, expected_result, expected_context",
    [
        (
            [
                "some_package/src/__init__.py",
                "some_package/src/utils_a.py",
                "some_package/src/utils_b.py",
                "some_package/src/utils_c.py",
            ],
            [
                "some_package/tests/__init__.py",
                "some_package/tests/test_utils_a.py",
                "some_package/tests/test_utils_b.py",
            ],
            [
                (
                    "some_package/src/utils_a.py",
                    "some_package/tests/test_utils_a.py",
                ),
                (
                    "some_package/src/utils_b.py",
                    "some_package/tests/test_utils_b.py",
                ),
            ],
            does_not_raise(),
        ),
    ],
)
def test_find_matching_files(
    src_files, test_files, expected_result, expected_context
) -> None:
    with expected_context:
        assert io.find_matching_files(src_files, test_files) == expected_result


@pytest.mark.parametrize(
    "current_location, src_folder, test_folder, expected_result, expected_context",
    [
        (
            get_dir_path(__file__, 0, "mock_package"),
            "mock_package/src",
            "mock_package/tests",
            [
                (
                    get_dir_path(__file__, 0, "mock_package/src/utils_a.py"),
                    get_dir_path(
                        __file__, 0, "mock_package/tests/test_utils_a.py"
                    ),
                )
            ],
            does_not_raise(),
        ),
    ],
)
def test_get_matching_files(
    current_location,
    src_folder,
    test_folder,
    expected_result,
    expected_context,
) -> None:
    with expected_context:
        assert (
            io.get_matching_files(current_location, src_folder, test_folder)
            == expected_result
        )

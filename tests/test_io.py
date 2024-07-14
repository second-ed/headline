from contextlib import nullcontext as does_not_raise

import pytest
from headline import io


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

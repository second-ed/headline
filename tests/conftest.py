from typing import List

import libcst as cst
import pytest
from headline import io
from headline._logger import get_dir_path
from headline.transform import _get_src_module, _get_visitor


@pytest.fixture
def get_fixture_test_utils_a_alphabetical():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/test_utils_a_alphabetical.py")
    )


@pytest.fixture
def get_fixture_test_utils_a_alphabetical_rename():
    return io.get_src_code(
        get_dir_path(
            __file__, 1, "mock_data/test_utils_a_alphabetical_rename.py"
        )
    )


@pytest.fixture
def get_fixture_test_utils_a_alphabetical_underscores():
    return io.get_src_code(
        get_dir_path(
            __file__, 1, "mock_data/test_utils_a_alphabetical_underscores.py"
        )
    )


@pytest.fixture
def get_fixture_test_utils_a_alphabetical_underscores_rename():
    return io.get_src_code(
        get_dir_path(
            __file__,
            1,
            "mock_data/test_utils_a_alphabetical_underscores_rename.py",
        )
    )


@pytest.fixture
def get_fixture_test_utils_a_called():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/test_utils_a_called.py")
    )


@pytest.fixture
def get_fixture_test_utils_a_called_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/test_utils_a_called_rename.py")
    )


@pytest.fixture
def get_fixture_test_utils_a_calls():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/test_utils_a_calls.py")
    )


@pytest.fixture
def get_fixture_test_utils_a_calls_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/test_utils_a_calls_rename.py")
    )


@pytest.fixture
def get_fixture_test_utils_a_newspaper():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/test_utils_a_newspaper.py")
    )


@pytest.fixture
def get_fixture_test_utils_a_newspaper_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/test_utils_a_newspaper_rename.py")
    )


@pytest.fixture
def get_fixture_test_utils_b_alphabetical():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/test_utils_b_alphabetical.py")
    )


@pytest.fixture
def get_fixture_test_utils_b_alphabetical_rename():
    return io.get_src_code(
        get_dir_path(
            __file__, 1, "mock_data/test_utils_b_alphabetical_rename.py"
        )
    )


@pytest.fixture
def get_fixture_test_utils_b_alphabetical_underscores():
    return io.get_src_code(
        get_dir_path(
            __file__, 1, "mock_data/test_utils_b_alphabetical_underscores.py"
        )
    )


@pytest.fixture
def get_fixture_test_utils_b_alphabetical_underscores_rename():
    return io.get_src_code(
        get_dir_path(
            __file__,
            1,
            "mock_data/test_utils_b_alphabetical_underscores_rename.py",
        )
    )


@pytest.fixture
def get_fixture_test_utils_b_called():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/test_utils_b_called.py")
    )


@pytest.fixture
def get_fixture_test_utils_b_called_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/test_utils_b_called_rename.py")
    )


@pytest.fixture
def get_fixture_test_utils_b_calls():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/test_utils_b_calls.py")
    )


@pytest.fixture
def get_fixture_test_utils_b_calls_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/test_utils_b_calls_rename.py")
    )


@pytest.fixture
def get_fixture_test_utils_b_manual():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/test_utils_b_manual.py")
    )


@pytest.fixture
def get_fixture_test_utils_b_manual_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/test_utils_b_manual_rename.py")
    )


@pytest.fixture
def get_fixture_test_utils_b_newspaper():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/test_utils_b_newspaper.py")
    )


@pytest.fixture
def get_fixture_test_utils_b_newspaper_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/test_utils_b_newspaper_rename.py")
    )


@pytest.fixture
def get_fixture_utils_a_alphabetical():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_a_alphabetical.py")
    )


@pytest.fixture
def get_fixture_utils_a_alphabetical_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_a_alphabetical_rename.py")
    )


@pytest.fixture
def get_fixture_utils_a_alphabetical_underscores():
    return io.get_src_code(
        get_dir_path(
            __file__, 1, "mock_data/utils_a_alphabetical_underscores.py"
        )
    )


@pytest.fixture
def get_fixture_utils_a_alphabetical_underscores_rename():
    return io.get_src_code(
        get_dir_path(
            __file__,
            1,
            "mock_data/utils_a_alphabetical_underscores_rename.py",
        )
    )


@pytest.fixture
def get_fixture_utils_a_called():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_a_called.py")
    )


@pytest.fixture
def get_fixture_utils_a_called_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_a_called_rename.py")
    )


@pytest.fixture
def get_fixture_utils_a_calls():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_a_calls.py")
    )


@pytest.fixture
def get_fixture_utils_a_calls_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_a_calls_rename.py")
    )


@pytest.fixture
def get_fixture_utils_a_newspaper():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_a_newspaper.py")
    )


@pytest.fixture
def get_fixture_utils_a_newspaper_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_a_newspaper_rename.py")
    )


@pytest.fixture
def get_fixture_utils_b_alphabetical():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_b_alphabetical.py")
    )


@pytest.fixture
def get_fixture_utils_b_alphabetical_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_b_alphabetical_rename.py")
    )


@pytest.fixture
def get_fixture_utils_b_alphabetical_underscores():
    return io.get_src_code(
        get_dir_path(
            __file__, 1, "mock_data/utils_b_alphabetical_underscores.py"
        )
    )


@pytest.fixture
def get_fixture_utils_b_alphabetical_underscores_rename():
    return io.get_src_code(
        get_dir_path(
            __file__,
            1,
            "mock_data/utils_b_alphabetical_underscores_rename.py",
        )
    )


@pytest.fixture
def get_fixture_utils_b_called():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_b_called.py")
    )


@pytest.fixture
def get_fixture_utils_b_called_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_b_called_rename.py")
    )


@pytest.fixture
def get_fixture_utils_b_calls():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_b_calls.py")
    )


@pytest.fixture
def get_fixture_utils_b_calls_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_b_calls_rename.py")
    )


@pytest.fixture
def get_fixture_utils_b_manual():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_b_manual.py")
    )


@pytest.fixture
def get_fixture_utils_b_manual_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_b_manual_rename.py")
    )


@pytest.fixture
def get_fixture_utils_b_newspaper():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_b_newspaper.py")
    )


@pytest.fixture
def get_fixture_utils_b_newspaper_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_b_newspaper_rename.py")
    )


@pytest.fixture
def get_fixture_utils_c_alphabetical():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_c_alphabetical.py")
    )


@pytest.fixture
def get_fixture_utils_c_alphabetical_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_c_alphabetical_rename.py")
    )


@pytest.fixture
def get_fixture_utils_c_alphabetical_underscores():
    return io.get_src_code(
        get_dir_path(
            __file__, 1, "mock_data/utils_c_alphabetical_underscores.py"
        )
    )


@pytest.fixture
def get_fixture_utils_c_alphabetical_underscores_rename():
    return io.get_src_code(
        get_dir_path(
            __file__,
            1,
            "mock_data/utils_c_alphabetical_underscores_rename.py",
        )
    )


@pytest.fixture
def get_fixture_utils_c_called():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_c_called.py")
    )


@pytest.fixture
def get_fixture_utils_c_called_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_c_called_rename.py")
    )


@pytest.fixture
def get_fixture_utils_c_calls():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_c_calls.py")
    )


@pytest.fixture
def get_fixture_utils_c_calls_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_c_calls_rename.py")
    )


@pytest.fixture
def get_fixture_utils_c_newspaper():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_c_newspaper.py")
    )


@pytest.fixture
def get_fixture_utils_c_newspaper_rename():
    return io.get_src_code(
        get_dir_path(__file__, 1, "mock_data/utils_c_newspaper_rename.py")
    )


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

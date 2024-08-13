from contextlib import nullcontext as does_not_raise

import headline.transform as tf
import libcst as cst
import pytest
from headline.visitors.func_visitors import FuncVisitor


@pytest.mark.parametrize(
    "fixture_name, results_names, expected_context",
    [
        (
            "get_fixture_utils_a_alphabetical",
            "get_utils_a_visitor_expected_attrs",
            does_not_raise(),
        ),
        (
            "get_fixture_test_utils_a_alphabetical",
            "get_test_utils_a_visitor_expected_attrs",
            does_not_raise(),
        ),
        (
            "get_fixture_mock_service",
            "get_mock_service_visitor_expected_attrs",
            does_not_raise(),
        ),
    ],
)
def test_func_visitor(request, fixture_name, results_names, expected_context):
    with expected_context:

        src_code = request.getfixturevalue(fixture_name)
        fv = tf._get_visitor(cst.parse_module(src_code))
        fv.process_func_defs()
        expected_results = request.getfixturevalue(results_names)
        assert isinstance(fv, FuncVisitor)
        assert fv.imports == expected_results["imports"]
        assert list(fv.func_defs.keys()) == expected_results["func_def_keys"]
        assert fv.top_level_funcs == expected_results["top_level_funcs"]

from contextlib import nullcontext as does_not_raise

import pytest
from headline.visitors.func_visitors import FuncVisitor


@pytest.mark.parametrize(
    "fixture_name, results_names, expected_context",
    [
        (
            "get_utils_a_visitor",
            "get_utils_a_visitor_expected_attrs",
            does_not_raise(),
        ),
        (
            "get_test_utils_a_visitor",
            "get_test_utils_a_visitor_expected_attrs",
            does_not_raise(),
        ),
    ],
)
def test_func_visitor(request, fixture_name, results_names, expected_context):
    with expected_context:

        fv = request.getfixturevalue(fixture_name)
        expected_results = request.getfixturevalue(results_names)
        assert isinstance(fv, FuncVisitor)
        assert fv.imports == expected_results["imports"]
        assert list(fv.func_defs.keys()) == expected_results["func_def_keys"]
        assert fv.top_level_funcs == expected_results["top_level_funcs"]
        # assert fv.calls == expected_results["calls"]
        # assert fv.called_by == expected_results["called_by"]

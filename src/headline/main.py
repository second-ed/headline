# import logging
# from src.headline.config import Config
# from src.headline._logger import (
#     get_dir_path,
#     setup_logger,
# )

# Config().set_filepath(get_dir_path(__file__, 2, "configs/example_config.yaml"))

# setup_logger(__file__, 2)
# logger = logging.getLogger()


import libcst as cst

from headline.transformers.func_transformers import FuncTransformer
from headline.utils import sort_func_names
from headline.visitors.func_visitors import (
    FuncCall,
    FuncVisitor,
)


def sort_src_functions(src_code: str) -> str:
    module = cst.parse_module(src_code)
    visitor = FuncVisitor()

    module.visit(visitor)

    all_local_funcs = [*visitor.top_level_funcs, *visitor.internal_funcs]
    local_calls = [c for c in visitor.is_called if c in all_local_funcs]

    # these need underscores added if they don't have them
    top_level_calls = {
        f: [c for c in visitor.calls[f] if c in visitor.top_level_funcs]
        for f in all_local_funcs
    }

    # these need underscores removed if they have them
    top_level_called = {
        f: [c for c in visitor.called_by[f] if c in visitor.top_level_funcs]
        for f in all_local_funcs
    }

    func_objs = []

    for f in all_local_funcs:
        if f in visitor.top_level_funcs:
            func_objs.append(
                FuncCall(
                    f,
                    top_level_calls[f],
                    top_level_called[f],
                )
            )

    sorted_funcs = sort_func_names(func_objs)

    transformer = FuncTransformer(
        {f.name: visitor.func_defs[f.name] for f in sorted_funcs},
        [f.name for f in sorted_funcs],
        all_local_funcs,
        [*local_calls, *visitor.internal_funcs],
    )

    modified_tree = module.visit(transformer)
    return modified_tree.code

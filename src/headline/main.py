# import logging
# from src.headline.config import Config
# from src.headline._logger import (
#     get_dir_path,
#     setup_logger,
# )

# Config().set_filepath(get_dir_path(__file__, 2, "configs/example_config.yaml"))

# setup_logger(__file__, 2)
# logger = logging.getLogger()

import inspect
from collections import defaultdict

import libcst as cst
from class_inspector import _utils

from headline.transformers.func_transformers import (
    DefSorter,
    PrivateDefStripper,
)
from headline.utils import remove_duplicate_calls, sort_func_names
from headline.visitors.func_visitors import (
    DefCollector,
    FuncCall,
    FuncCallCollector,
)

source_code = inspect.getsource(_utils)
module = cst.parse_module(source_code)
def_collector = DefCollector()
module.visit(def_collector)

func_calls = defaultdict(list)
called_by = defaultdict(list)

for func_name, func_node in def_collector.func_defs.items():
    call_collector = FuncCallCollector(def_collector.def_names)
    func_node.body.visit(call_collector)
    func_calls[func_name] = call_collector.calls

    for called_func in call_collector.calls:
        called_by[called_func].append(func_name)


funcs = []

for func_name, calls in func_calls.items():
    funcs.append(
        FuncCall(
            func_name,
            remove_duplicate_calls(calls),
            remove_duplicate_calls(called_by[func_name]),
        )
    )

sorted_funcs = sort_func_names(funcs)

transformer = DefSorter(
    [def_collector.func_defs[f.name] for f in sorted_funcs]
)
modified_tree = module.visit(transformer)

transformer2 = PrivateDefStripper(
    [f.name for f in funcs if f.name.startswith("_") and len(f.called) != 0]
)
modified_tree = modified_tree.visit(transformer2)

print(modified_tree.code)

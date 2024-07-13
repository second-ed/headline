from collections import defaultdict

import attr
import libcst as cst
from attr.validators import instance_of

from headline.utils import remove_duplicate_calls


@attr.define
class FuncDef:
    name: str = attr.ib(validator=[instance_of(str)])
    def_code: cst.FunctionDef = attr.ib(
        validator=[instance_of(cst.FunctionDef)]
    )
    calls: list = attr.ib(validator=[instance_of(list)])
    called: list = attr.ib(validator=[instance_of(list)])
    indent: int = attr.ib(validator=[instance_of(int)])


@attr.define
class FuncVisitor(cst.CSTVisitor):
    func_defs: dict = attr.ib(default=None)
    is_called: list = attr.ib(default=None)
    depth: int = attr.ib(default=0, validator=[instance_of(int)])  # type: ignore
    curr_func: str = attr.ib(default="")
    calls: dict = attr.ib(default=None)
    called_by: dict = attr.ib(default=None)
    top_level_funcs: list = attr.ib(validator=[instance_of(list)], init=False)

    def __attrs_post_init__(self):
        self.func_defs = {}
        self.is_called = []
        self.calls = defaultdict(list)
        self.called_by = defaultdict(list)

    def visit_FunctionDef(self, node: cst.FunctionDef) -> None:
        self.curr_func = node.name.value
        self.func_defs[node.name.value] = FuncDef(
            node.name.value, node, [], [], self.depth
        )

    def visit_IndentedBlock(self, node: cst.IndentedBlock) -> None:
        self.depth += 1

    def leave_IndentedBlock(self, node: cst.IndentedBlock) -> None:
        self.depth -= 1

    def visit_Call(self, node: cst.Call) -> None:
        if isinstance(node.func, cst.Name):
            self.calls[self.curr_func].append(node.func.value)
            self.called_by[node.func.value].append(self.curr_func)
            self.is_called.append(node.func.value)

    def process_func_defs(self) -> None:
        self.top_level_funcs = [
            f.name for f in self.func_defs.values() if f.indent == 0
        ]

        for f in self.func_defs:
            self.func_defs[f].calls = remove_duplicate_calls(
                [c for c in self.calls[f] if c in self.top_level_funcs]
            )
            self.func_defs[f].called = remove_duplicate_calls(
                [c for c in self.called_by[f] if c in self.top_level_funcs]
            )

from collections import defaultdict

import attr
import libcst as cst
from attr.validators import instance_of


@attr.define(frozen=True)
class FuncCall:
    name: str = attr.ib(validator=[instance_of(str)])
    calls: list = attr.ib(validator=[instance_of(list)])
    called: list = attr.ib(validator=[instance_of(list)])


@attr.define
class FuncVisitor(cst.CSTVisitor):
    top_level_funcs: list = attr.ib(default=None)
    internal_funcs: list = attr.ib(default=None)
    func_defs: dict = attr.ib(default=None)
    calls: dict = attr.ib(default=None)
    called_by: dict = attr.ib(default=None)
    is_called: list = attr.ib(default=None)
    depth: int = attr.ib(default=0, validator=[instance_of(int)])  # type: ignore
    curr_func: str = attr.ib(default="")

    def __attrs_post_init__(self):
        self.top_level_funcs = []
        self.internal_funcs = []
        self.is_called = []
        self.calls = defaultdict(list)
        self.called_by = defaultdict(list)
        self.func_defs = {}

    def visit_FunctionDef(self, node: cst.FunctionDef) -> None:
        if self.depth == 0:
            self.curr_func = node.name.value
            self.top_level_funcs.append(node.name.value)
            self.func_defs[node.name.value] = node
        else:
            self.internal_funcs.append(node.name.value)

    def visit_IndentedBlock(self, node: cst.IndentedBlock) -> None:
        self.depth += 1

    def leave_IndentedBlock(self, node: cst.IndentedBlock) -> None:
        self.depth -= 1

    def visit_Call(self, node: cst.Call) -> None:
        if isinstance(node.func, cst.Name):
            self.calls[self.curr_func].append(node.func.value)
            self.called_by[node.func.value].append(self.curr_func)
            self.is_called.append(node.func.value)

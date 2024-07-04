import attr
import libcst as cst
from attr.validators import instance_of, optional


@attr.define(frozen=True)
class FuncCall:
    name: str = attr.ib(validator=[instance_of(str)])
    calls: list = attr.ib(validator=[instance_of(list)])
    called: list = attr.ib(validator=[instance_of(list)])


@attr.define
class DefCollector(cst.CSTVisitor):
    depth: int = attr.ib(default=0, validator=[instance_of(int)])
    def_names: list = attr.ib(
        default=None, validator=[optional(instance_of(list))]
    )
    func_defs: dict = attr.ib(
        default=None, validator=[optional(instance_of(dict))]
    )

    def __attrs_post_init__(self):
        self.def_names = []
        self.func_defs = {}

    def visit_FunctionDef(self, node: cst.FunctionDef) -> None:
        if self.depth == 0:
            self.def_names.append(node.name.value)
            self.func_defs[node.name.value] = node

    def visit_IndentedBlock(self, node: cst.IndentedBlock) -> None:
        self.depth += 1

    def leave_IndentedBlock(self, node: cst.IndentedBlock) -> None:
        self.depth -= 1


@attr.define
class FuncCallCollector(cst.CSTVisitor):
    func_names: list = attr.ib(validator=[instance_of(list)])
    calls: list = attr.ib(
        default=None, validator=[optional(instance_of(list))]
    )

    def __attrs_post_init__(self):
        self.calls = []

    def visit_Call(self, node: cst.Call) -> None:
        if isinstance(node.func, cst.Name):
            func_name = node.func.value
            if func_name in self.func_names:
                self.calls.append(func_name)

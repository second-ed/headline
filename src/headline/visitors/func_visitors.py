from collections import defaultdict
from typing import Optional

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
    class_name: str = attr.ib(validator=[instance_of(str)])


@attr.define
class FuncVisitor(cst.CSTVisitor):
    imports: dict = attr.ib(default=None)
    func_defs: dict = attr.ib(default=None)
    is_called: list = attr.ib(default=None)
    depth: int = attr.ib(default=0, validator=[instance_of(int)])  # type: ignore
    curr_func: str = attr.ib(default="")
    curr_class: str = attr.ib(default="")
    calls: dict = attr.ib(default=None)
    called_by: dict = attr.ib(default=None)
    classes_methods: dict = attr.ib(default=None)
    top_level_funcs: list = attr.ib(validator=[instance_of(list)], init=False)

    def __attrs_post_init__(self):
        self.imports = {}
        self.func_defs = {}
        self.is_called = []
        self.calls = defaultdict(list)
        self.called_by = defaultdict(list)
        self.classes_methods = defaultdict(list)

    def visit_Import(self, node: cst.Import):
        for alias in node.names:
            name = alias.name.value
            asname = alias.asname.name.value if alias.asname else name
            self.imports[name] = {"name": name, "as_name": asname}

    def visit_ImportFrom(self, node: cst.ImportFrom):
        module = self._get_full_module_name(node.module)
        for alias in node.names:
            name = alias.name.value
            asname = alias.asname.name.value if alias.asname else name
            self.imports[module] = {"name": name, "as_name": asname}

    def visit_FunctionDef(self, node: cst.FunctionDef) -> None:
        self.curr_func = node.name.value
        self.func_defs[node.name.value] = FuncDef(
            node.name.value, node, [], [], self.depth, self.curr_class
        )

    def visit_IndentedBlock(self, node: cst.IndentedBlock) -> None:
        self.depth += 1

    def leave_IndentedBlock(self, node: cst.IndentedBlock) -> None:
        self.depth -= 1

    def visit_ClassDef(self, node: cst.ClassDef) -> None:
        self.curr_class = node.name.value

    def leave_ClassDef(self, node: cst.ClassDef) -> None:
        self.curr_class = ""

    def visit_Call(self, node: cst.Call) -> None:
        if isinstance(node.func, cst.Name):
            self.calls[self.curr_func].append(node.func.value)
            self.called_by[node.func.value].append(self.curr_func)
            self.is_called.append(node.func.value)

    def process_func_defs(self) -> None:
        self.top_level_funcs = [
            f.name
            for f in self.func_defs.values()
            if f.indent == 0 and not f.class_name
        ]

        for f, func in self.func_defs.items():
            self.func_defs[f].calls = remove_duplicate_calls(
                [c for c in self.calls[f] if c in self.top_level_funcs]
            )
            self.func_defs[f].called = remove_duplicate_calls(
                [c for c in self.called_by[f] if c in self.top_level_funcs]
            )
            if func.class_name:
                self.classes_methods[func.class_name].append(func.name)

    def _get_full_module_name(self, module) -> Optional[str]:
        if isinstance(module, cst.Attribute):
            return (
                self._get_full_module_name(module.value)
                + "."
                + module.attr.value
            )
        elif isinstance(module, cst.Name):
            return module.value
        return None

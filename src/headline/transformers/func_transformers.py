import logging

import attr
import libcst as cst
from attr.validators import instance_of

from headline.utils import (
    get_func_name_edit,
    get_leading_lines,
)

logger = logging.getLogger()


@attr.define
class FuncTransformer(cst.CSTTransformer):
    func_defs: dict = attr.ib(validator=[instance_of(dict)])
    sorted_func_names: list = attr.ib(validator=[instance_of(list)])
    private_funcs: list = attr.ib(validator=[instance_of(list)], init=False)
    rename_funcs: bool = attr.ib(default=True, validator=[instance_of(bool)])  # type: ignore
    def_index: int = attr.ib(default=0, validator=[instance_of(int)])  # type: ignore

    def __attrs_post_init__(self):
        self.private_funcs = [
            f.name
            for f in self.func_defs.values()
            if (f.indent > 0) or (len(f.called) > 0)
        ]

    def leave_Module(
        self, original_node: cst.Module, updated_node: cst.Module
    ) -> cst.Module:
        """this reorders functions based on the sorted_func_defs and
        ensures that they each have 2 new lines of between definitions

        Args:
            original_node (cst.Module)
            updated_node (cst.Module)

        Returns:
            cst.Module
        """
        new_body = []
        for element in updated_node.body:
            # checking against -1 to account for more functions that aren't in the
            # sorted list (e.g. when comparing src names to tests)
            if (
                isinstance(element, cst.FunctionDef)
                and len(self.sorted_func_names) > self.def_index
            ):
                # get the sorted function by index and remove leading_lines to avoid
                # functions having more than 2 lines between them
                new_func = self.func_defs[
                    self.sorted_func_names[self.def_index]
                ].def_code.with_changes(
                    leading_lines=get_leading_lines(self.def_index)
                )
                new_body.append(new_func)
                new_body.extend([cst.EmptyLine(), cst.EmptyLine()])
                self.def_index += 1
            else:
                new_body.append(element)
        return updated_node.with_changes(
            body=new_body,
        )

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        if self.rename_funcs:
            func_name = updated_node.name.value
            name_edit = get_func_name_edit(
                func_name, list(self.func_defs.keys()), self.private_funcs
            )
            # logger.debug(f"{func_name = }")
            # logger.debug(f"{list(self.func_defs.keys()) = }")
            # logger.debug(f"{self.private_funcs = }")
            # logger.debug(f"{name_edit = }")

            if name_edit and func_name in self.func_defs:
                updated_node = updated_node.with_changes(
                    name=cst.Name(value=name_edit)
                )
                self.func_defs[func_name].def_code = updated_node
        return updated_node

    def leave_Call(
        self, original_node: cst.Call, updated_node: cst.Call
    ) -> cst.CSTNode:
        if isinstance(updated_node.func, cst.Name) and self.rename_funcs:

            name_edit = get_func_name_edit(
                updated_node.func.value,
                list(self.func_defs.keys()),
                self.private_funcs,
            )
            if name_edit and updated_node.func.value in self.func_defs:
                updated_node = updated_node.with_changes(
                    func=cst.Name(value=name_edit)
                )
        return updated_node

    def leave_Arg(
        self, original_node: cst.Arg, updated_node: cst.Arg
    ) -> cst.Arg:
        if isinstance(updated_node.value, cst.Name) and self.rename_funcs:
            func_name = updated_node.value.value

            if func_name in self.func_defs:
                name_edit = get_func_name_edit(
                    func_name, list(self.func_defs.keys()), self.private_funcs
                )
                if name_edit:
                    updated_node = updated_node.with_changes(
                        value=cst.Name(value=name_edit)
                    )
                # self.func_defs[func_name].def_code = updated_node
        return updated_node

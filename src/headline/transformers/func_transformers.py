import attr
import libcst as cst
from attr.validators import instance_of

from headline.utils import (
    get_func_name_edit,
    get_leading_lines,
)


@attr.define
class FuncTransformer(cst.CSTTransformer):
    func_defs: dict = attr.ib(validator=[instance_of(dict)])
    sorted_func_names: list = attr.ib(validator=[instance_of(list)])
    all_funcs: list = attr.ib(validator=[instance_of(list)])
    private_funcs: list = attr.ib(validator=[instance_of(list)])
    def_index: int = attr.ib(default=0, validator=[instance_of(int)])  # type: ignore

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
            if isinstance(element, cst.FunctionDef):
                # get the sorted function by index and remove leading_lines to avoid
                # functions having more than 2 lines between them

                new_func = self.func_defs[
                    self.sorted_func_names[self.def_index]
                ].with_changes(leading_lines=get_leading_lines(self.def_index))
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
        func_name = updated_node.name.value
        name_edit = get_func_name_edit(
            func_name, self.all_funcs, self.private_funcs
        )
        if name_edit:
            updated_node = updated_node.with_changes(
                name=cst.Name(value=name_edit)
            )
        self.func_defs[func_name] = updated_node
        return updated_node

    def leave_Call(
        self, original_node: cst.Call, updated_node: cst.Call
    ) -> cst.CSTNode:
        if isinstance(updated_node.func, cst.Name):
            name_edit = get_func_name_edit(
                updated_node.func.value, self.all_funcs, self.private_funcs
            )
            if name_edit:
                updated_node = updated_node.with_changes(
                    func=cst.Name(value=name_edit)
                )
        return updated_node

    def leave_Arg(
        self, original_node: cst.Arg, updated_node: cst.Arg
    ) -> cst.Arg:
        if isinstance(updated_node.value, cst.Name):
            func_name = updated_node.value.value
            name_edit = get_func_name_edit(
                func_name, self.all_funcs, self.private_funcs
            )
            if name_edit:
                updated_node = updated_node.with_changes(
                    value=cst.Name(value=name_edit)
                )
            self.func_defs[func_name] = updated_node
        return updated_node

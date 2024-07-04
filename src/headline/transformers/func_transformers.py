import attr
import libcst as cst
from attr.validators import instance_of


@attr.define
class DefSorter(cst.CSTTransformer):
    sorted_func_defs: list = attr.ib(validator=[instance_of(list)])
    def_index: int = attr.ib(default=0, validator=[instance_of(int)])

    def leave_Module(
        self, original_node: cst.Module, updated_node: cst.Module
    ) -> cst.Module:
        new_body = []
        for element in updated_node.body:
            if isinstance(element, cst.FunctionDef):
                new_body.append(self.sorted_func_defs[self.def_index])
                self.def_index += 1
            else:
                new_body.append(element)
        return updated_node.with_changes(body=new_body)


@attr.define
class PrivateDefStripper(cst.CSTTransformer):
    private_funcs: list = attr.ib(validator=[instance_of(list)])

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        func_name = updated_node.name.value
        if func_name.startswith("_") and func_name not in self.private_funcs:
            updated_node = updated_node.with_changes(
                name=cst.Name(value=func_name.lstrip("_"))
            )
        return updated_node

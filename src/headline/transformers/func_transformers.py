import attr
import libcst as cst
from attr.validators import instance_of

from headline.utils import is_not_private_and_has_leading_underscore


@attr.define
class DefTransformer(cst.CSTTransformer):
    sorted_func_defs: list = attr.ib(validator=[instance_of(list)])
    funcs: list = attr.ib(validator=[instance_of(list)])
    all_funcs: list = attr.ib(validator=[instance_of(list)], init=False)
    private_funcs: list = attr.ib(validator=[instance_of(list)], init=False)
    def_index: int = attr.ib(default=0, validator=[instance_of(int)])

    def __attrs_post_init__(self):
        self.all_funcs = [f.name for f in self.funcs]
        self.private_funcs = [
            f.name
            for f in self.funcs
            if f.name.startswith("_") and len(f.called) != 0
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
            if isinstance(element, cst.FunctionDef):
                # get the sorted function by index and remove leading_lines to avoid
                # functions having more than 2 lines between them
                new_func = self.sorted_func_defs[self.def_index].with_changes(
                    leading_lines=[]
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
        func_name = updated_node.name.value
        if is_not_private_and_has_leading_underscore(
            func_name, self.all_funcs, self.private_funcs
        ):
            updated_node = updated_node.with_changes(
                name=cst.Name(value=func_name.lstrip("_"))
            )
        return updated_node

    def leave_Call(
        self, original_node: cst.Call, updated_node: cst.Call
    ) -> cst.CSTNode:
        if isinstance(
            original_node.func, cst.Name
        ) and is_not_private_and_has_leading_underscore(
            original_node.func.value, self.all_funcs, self.private_funcs
        ):
            updated_node = updated_node.with_changes(
                func=cst.Name(value=original_node.func.value.lstrip("_"))
            )
        return updated_node

def remove_duplicate_calls(calls: list) -> list:
    return list(dict.fromkeys(calls))


def sort_func_names(funcs):
    return sorted(
        funcs, key=lambda x: (-len(x.calls), -len(x.called), x.name.strip("_"))
    )


def is_not_private_and_has_leading_underscore(
    func_name: str, all_funcs: list, private_funcs: list
) -> bool:
    return (
        func_name.startswith("_")
        and func_name in all_funcs
        and func_name not in private_funcs
    )


def is_private_and_has_no_leading_underscore(
    func_name: str, all_funcs: list, private_funcs: list
) -> bool:
    return (
        not func_name.startswith("_")
        and func_name in all_funcs
        and func_name in private_funcs
    )

def remove_duplicate_calls(calls: list) -> list:
    return list(dict.fromkeys(calls))


def sort_func_names(funcs):
    return sorted(funcs, key=lambda x: (len(x.called), -len(x.calls), x.name))

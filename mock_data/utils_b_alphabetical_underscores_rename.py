
def _b():
    return 0


def _a():
    return 1


def c():
    _a()


def d():
    res = _a() + _b()
    return res


def e():
    _b()



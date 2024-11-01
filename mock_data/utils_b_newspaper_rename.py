
def d():
    res = _a() + _b()
    return res


def c():
    _a()


def e():
    _b()


def _a():
    return 1


def _b():
    return 0



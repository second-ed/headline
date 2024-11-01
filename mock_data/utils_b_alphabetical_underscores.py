
def _b():
    return 0


def a():
    return 1


def c():
    a()


def d():
    res = a() + _b()
    return res


def e():
    _b()



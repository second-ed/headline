
def d():
    res = a() + _b()
    return res


def c():
    a()


def e():
    _b()


def _b():
    return 0


def a():
    return 1



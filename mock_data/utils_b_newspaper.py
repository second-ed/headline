
def d():
    res = a() + _b()
    return res


def c():
    a()


def e():
    _b()


def a():
    return 1


def _b():
    return 0



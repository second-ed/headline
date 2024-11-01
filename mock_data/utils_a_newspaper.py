
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result = multiply(result, i)
    return result


def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, add(a, b)
    return b


def power(base, exponent):
    if exponent < 0:
        raise ValueError("Exponent should be non-negative")
    result = 1
    for _ in range(exponent):
        result = multiply(result, base)
    return result


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def _subtract(a, b):
    return a - b


def multiply(a, b):
    res = 0
    for _ in range(b):
        res = add(res, a)

    return res


def add(a, b):
    return a + b



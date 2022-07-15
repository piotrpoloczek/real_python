def _recurse_factorial(num):
    if num <= 1:
        return 1

    return num * _recurse_factorial(num - 1)

def first_factorial(num):
    if not isinstance(num, int):
        raise TypeError("Bad parameter, 'num' must be an integer")

    if num < 0:
        raise ValueError("Bad parameter, 'num' must be >= 0")

    return _recurse_factorial(num)
def second_factorial(num):
    if not isinstance(num, int):
        raise TypeError("Bad parameter, 'num' must be an integer")

    if num < 0:
        raise ValueError("Bad parameter, 'num' must be >= 0")

    def inner_factorial(num):
        if num <= 1:
            return 1

        return num * inner_factorial(num - 1)

    return inner_factorial(num)
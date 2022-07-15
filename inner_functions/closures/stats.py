def even_meaner():
    sample = []
    current = 0

    def inner_mean(number):
        nonlocal current

        sample.append(number)
        current = sum(sample) / float(len(sample))
        return current

    def value():
        nonlocal current
        return current

    def reset():
        nonlocal sample, current
        current = 0
        sample = []

    inner_mean.value = value
    inner_mean.reset = reset

    return inner_mean
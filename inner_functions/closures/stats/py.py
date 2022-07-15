def mean():
    sample = []

    def inner_mean(number):
        sample.append(number)
        return sum(sample) / float(len(sample))

    return inner_mean
from math import prod


def largest_product(series, size):
    maximum = 0
    if len(series) < size or size < 0:
        raise ValueError('size is greater than series')
    else:
        for i in range(0, len(series) - size + 1):
            num_str = series[i:i+size]
            local_max = prod([int(j) for j in num_str])
            if local_max > maximum:
                maximum = local_max
    return maximum

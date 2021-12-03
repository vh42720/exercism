def square(number):
    if number > 64 or number <= 0:
        raise ValueError('Value does not make sense')
    return 2 ** (number - 1)


def total():
    # using math formula calculating sum of 2 powers from 0 to n
    return 2 ** 64 - 1

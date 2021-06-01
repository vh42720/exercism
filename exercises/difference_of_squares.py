def square_of_sum(number):
    return sum([i for i in range(number+1)])**2


def sum_of_squares(number):
    return (number * (number + 1) * (2 * number + 1)) / 6


def difference_of_squares(number):
    return abs(sum_of_squares(number) - square_of_sum(number))

def is_armstrong_number(number):
    power = len(str(number))
    sum_pow = sum([int(digit) ** power for digit in str(number)])
    return sum_pow == number


print(is_armstrong_number(9926315))

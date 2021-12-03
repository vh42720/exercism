# diving by first prime and moving up
def factors(value):
    factors_list = []
    prime = 2
    while value > 1:
        while value % prime == 0:
            factors_list.append(prime)
            value /= prime
        prime += 1

    return factors_list


print(factors(93819012551))

import numpy as np
from itertools import compress


def primes(limit):
    nums = [i for i in range(2, limit+1)]
    idx = [True] * (limit - 1)
    # cross out any multiples of 2
    for i in range(2, int(np.sqrt(limit))+1):
        if idx[i-2]:
            for j in np.arange(i**2, limit+1, i):
                idx[j-2] = False

    return list(compress(nums, idx))


print(primes(10))

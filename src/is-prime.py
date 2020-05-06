
""" @docStart
### Prime Numbers
@docEnd """

# @codeStart

import math


def isPrime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    l = int(math.sqrt(x))
    if x % l == 0:
        return False
    i = 3
    while i <= l:
        if x % i == 0:
            return False
        i += 2
    return True

# @codeEnd
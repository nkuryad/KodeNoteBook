
""" @docStart
### Factorials
@docEnd """

# @codeStart

from functools import reduce

# returns factorial


def factorial(x):
    res = 1
    while x >= 1:
        res = res*x
        x -= 1
    return res


print(factorial(10))
# 362880
# @codeEnd
""" @docStart
##### Factorials Using Recursive Function
@docEnd """
# @codeStart
def factorialR(x):
    if x != 1:
        return x*factorialR(x-1)
    else:
        return 1

print(factorialR(10))
# 3628800

# @codeEnd
""" @docStart
##### One liner using reduce and lambda
@docEnd """
# @codeStart
def factorialO(x):
    return reduce(lambda a, b: a*b, range(1, x+1), 1)

print(factorialO(10))
# 3628800

# @codeEnd

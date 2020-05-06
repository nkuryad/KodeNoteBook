
""" @docStart
### List Sum
@docEnd """

# @codeStart

from functools import reduce


# sum of all parameters
def sumAll(*x):
    res = 0
    for a in x:
        res += a
    return res


print(sumAll(2, 3, 4, 5))
# 14


# sum of no. of given list
def listSum(x):
    res = 0
    for i in x:
        res += i
    return res


print(listSum([2, 3, 4, 5]))
# 14


# One liner using reduce and lambda
def listSumO(x): return reduce(lambda a, b: a+b, x, 0)


print(listSumO(range(1, 11)))
# 55

# @codeEnd

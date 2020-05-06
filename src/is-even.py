
""" @docStart
### Even Numbers
@docEnd """

# @codeStart

# check the given no. is even no. or not

def isEven(x): return x % 2 == 0


print(isEven(4))
# True
print(isEven(3))
# False

# filter even no. from list of numbers

def filterEven(x):
    res = []
    for i in x:
        if isEven(i):
            res.append(i)
    return res


print(filterEven(range(5, 11)))
# [6, 8, 10]


print(filterEven(range(2, 9)))
# [2, 4, 6, 8]

# oneline function for list of even no.from given range
def even(x): return list(filter(isEven, x))


print(even(range(30, 35)))
# [30, 32, 34]

# @codeEnd
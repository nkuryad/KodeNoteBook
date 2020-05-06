
""" @docStart
### Lists sum
@docEnd """

# @codeStart

# takes 2 list and sum all corresponding no.

def listsSum(x, y):
    res = []
    for i in range(0, len(x)):
        res.append(x[i]+y[i])
    return res


print(listsSum([2, 3, 5], [3, 2, 1]))
# [5, 5, 6]

# @codeEnd
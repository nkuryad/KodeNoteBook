
""" @docStart
### 2D-Lists Sum
@docEnd """

# @codeStart

# takes two 2D-lists and give the sum of its corresponding no.

def listsSum2d(x, y):
    result = []
    i = 0
    while i < len(x):
        res = []
        n = 0
        while n < len(x[i]):
            res.append(x[i][n]+y[i][n])
            n += 1
        result.append(res)
        i += 1
    return result


print(
    listsSum2d(
        [[2, 3, 4], [5, 6, 7]],
        [[2, 3, 4], [5, 6, 7]]
    )
)
# [[4, 6, 8], [10, 12, 14]]

# @codeEnd

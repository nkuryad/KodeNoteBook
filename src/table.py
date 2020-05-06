
""" @docStart
### Table Generator
@docEnd """

# @codeStart

def table(x):
    res = []
    for i in range(1, 11):
        res.append(x*i)
    return res


print(table(5))
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# oneliners style
def table(x): return list(range(x, 10*x+1, x))


print(table(5))

# @codeEnd

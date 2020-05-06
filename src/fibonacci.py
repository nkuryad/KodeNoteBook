
""" @docStart
### Fibonacci
@docEnd """

# @codeStart


def fib(x):
    i = 1
    tmp = 0
    a = 0
    b = 1
    print(a)
    print(b)
    while i <= x-2:
        tmp = b
        b = a + b
        a = tmp
        print(b)
        i += 1


fib(10)
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55

# @codeEnd
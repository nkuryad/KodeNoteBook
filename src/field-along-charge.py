
""" @docStart
### Electric Field Along A Sphere
@docEnd """

# @codeStart

import math

# calculates electric field along a sphere

def eField(sigma, R, r):
    epsilon = 8.85e-12
    e = 0
    if r > R:
        e = (sigma/(4*math.pi*epsilon))*(R/r)**2
    elif r == R:
        e = sigma/epsilon
    return e


print(eField(5e-6, 6, 6))
# 564971.7514124294
print(eField(5e-6, 6, 5))
# 0
print(eField(5e-6, 6, 9))
# 19981.788209905255

# @codeEnd
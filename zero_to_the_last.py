"""
Given an array of random numbers, Push all the Zero's of a given array to the end of the array.
ex: {1,9,8,4,0,0,2,7,0,6,0}
o/p: {1,9,8,4,2,7,6,0,0,0,0}
"""

def fun(x):
    res = []
    for i in x:
        if i > 0:
            res.append(i)

    for i in range(len(x)-len(res)):
        res.append(0)

    return res

print(fun([1,9,8,4,0,0,2,7,0,6,0]))


"""
OUTPUT:
>>> [1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0]
"""

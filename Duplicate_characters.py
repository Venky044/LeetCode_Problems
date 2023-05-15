"""
Write a program to find duplicate characters in the String.
ex: 'I came for interview'
o/p: i-3, e-3, r-2
"""

def fun(x):
    n = []
    x = x.lower()
    for el in x:
        if x.count(el) > 1 and el not in n and el != ' ':
            n.append(el)
            no_dup = x.count(el)
            print(f'{el}-{no_dup}')
    

st = 'I came for interview'
fun(st)


"""
OUTPUT:
e-3
r-2
i-2
"""
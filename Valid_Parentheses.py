"""
Given a string s = ['(',')','[',']','{','}']
determine if the given input string is valid
if valid:
    open brackets must be closed with its same type

    Input: s = '()'
    Output: true

    Input: s = "()[]{}"
    Output: true

    Input: s = "(]"
    Output: false
"""


# 1st way to solving this problem.
def sameparanthasis(str):
    s = "()[]{}"
    i = 0
    valid = "true"
    while i < len(str):
        x = s.index(str[i])
        if i + 1 < len(str) and str[i + 1] == s[x + 1]:
            valid = "true"
            i += 2
        else:
            valid = "false"
            i += 1
    return valid


n = "{[]}"
# print(sameparanthasis(n))

# -------------------------------------------------


# 2nd way to solving this problem.
def solution(n):
    if len(n) % 2 != 0:
        return False
    dic = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for i in n:
        if i in dic.keys():
            stack.append(i)
        else:
            if stack is None:
                return False
            s = stack.pop()
            if i != dic[s]:
                return False
    return stack == []


n = "(]"
# print(solution(n))

# --------------


# 3rd way to solving this problem.
def fun(s):
    if len(s) % 2 != 0:
        return False

    dic = {"(": ")", "[": "]", "{": "}"}

    x = []
    for i in s:
        if i in dic.keys():
            x.append(i)

        else:
            k = len(x) - 1
            if i == dic[x[k]]:
                x = x[:k]

    if len(x):
        return False
    else:
        return True


s = "([)]"
# s = "()[]{}"
# s = "(]"
# s = '([{()})'

# print(fun(s))

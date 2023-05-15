"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

"""


def sol(a1, b1):
    res = []
    carry = 0

    i = len(a1) - 1
    j = len(b1) - 1

    while i >= 0 or j >= 0:
        s1 = int(a1[i]) if i >= 0 else 0
        s2 = int(b1[j]) if j >= 0 else 0

        total = s1 + s2 + carry
        val = total % 2
        carry = total // 2
        res.insert(0, str(val))

        i -= 1
        j -= 1

    if carry:
        res.insert(0, "1")

    return "".join(res)


# a = "1010"
# b = "1011"
# print(sol(a, b))

# --------------------------------


# 2nd way to solving this problem.
def sol1(a1, b1):
    res = ""
    carry = 0
    a, b = a1[::-1], b1[::-1]
    for i in range(max(len(a), len(b))):
        s1 = int(a[i]) if i < len(a) else 0
        s2 = int(b[i]) if i < len(b) else 0

        total = s1 + s2 + carry
        val = total % 2
        carry = total // 2
        res += str(val)

    if carry:
        res += "1"

    return res[::-1]


# a = "11"
# b = "1"

# a = "1010"
# b = "1011"
# print(sol1(a, b))

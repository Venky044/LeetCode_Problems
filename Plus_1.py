#       Plus One

"""
    You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

"""
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].


Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].


Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""


# 1st way to solving this problem.
def sol(n):
    if n[-1] < 9:
        n[-1] = n[-1] + 1
        return n

    s = ""
    for i in n:
        s += str(i)

    x = int(s) + 1
    n = [int(i) for i in str(x)]
    # y = [int(i) for i in str(int(s)+1)]
    return n


# n = [4, 3, 2, 1]
# n = [9,9,9]
# n = [1,2,3]

# print(sol(n))
# --------------------------------------------------


# 2nd way to solving this problem.
def sol2(digits):
    digits = digits[::-1]
    one, ind = 1, 0
    while one:
        if ind < len(digits):
            if digits[ind] == 9:
                digits[ind] = 0
            else:
                digits[ind] += 1
                one = 0
        else:
            digits.append(1)
            one = 0
        ind += 1

    return digits[::-1]


# print(sol2(n))
# -------------------------------------------------------------------


# 2nd way to solving this problem.
def sol3(digits):
    i = len(digits)
    while i >= 0:
        i -= 1
        if i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        else:
            digits.insert(0, 1)
            return digits


# n2 = [1, 1, 9, 9]
# print(sol3(n2))

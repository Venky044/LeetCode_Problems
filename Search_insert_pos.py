#       Search Insert Position

"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

"""
Input: nums = [1,3,5,6], target = 5
Output: 2
"""

"""
Input: nums = [1,3,5,6], target = 2
Output: 1
"""

"""
Input: nums = [1,3,5,6], target = 7
Output: 4
"""


def search_in(num, tar):
    if len(num) == 0:
        return 0

    l = 0
    h = len(num) - 1
    while l <= h:
        mid = (l + h) // 2
        if num[mid] == tar:
            return mid

        if tar < num[mid]:
            h = mid - 1
        else:
            l = mid + 1

    return l


# num = [1, 3, 5, 6, 8, 9, 12]
# print(search_in(num, 13))
# -----------------------------------------


# 2nd way to solving this problem.
def search_in2(num, tar):
    if len(num) == 0:
        return 0

    if tar in num:
        return num.index(tar)

    for i in range(len(num)):
        if i + 1 <= len(num) - 1:
            if num[i] < tar and num[i + 1] > tar:
                return i + 1

        else:
            if tar > num[i]:
                return i + 1
            else:
                return i


# num = [2]
# print(search_in2(num, 1))

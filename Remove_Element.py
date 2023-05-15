#        Remove Element
"""
Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place. 
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

"""
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
"""

"""
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
"""


# 1st way to solving this problem.
class Solution:
    def removeElement(self, nums, val):
        x = []
        for i in nums:
            if i != val:
                x.append(i)
        k = len(x)
        nums[:k] = x[:]
        return k


# s = Solution()
# print(s.removeElement([3, 2, 2, 3], 3))
# ------------------------------------------


# 2nd way to solving this problem.
def remove_element(num, val):
    x = []
    for i in num:
        if i != val:
            x.append(i)
    k = len(x)
    num[:k] = x[:]
    return k, num


# num = [0, 1, 2, 2, 3, 0, 4, 2]
# print(remove_element(num, 2))
# ---------------------------------------------


# 3rd way to solving this problem.
def sol(nums, val):
    x = []
    for i in nums:
        if i != val:
            x.append(i)

    k = len(x)
    nums[:k] = x[:]

    x2 = [0 for _ in nums[k:]]
    nums[k:] = x2[:]

    return k, nums


# num = [3, 2, 2, 3]
# print(sol(num, 2))

#   Remove Duplicates from Sorted Array

"""
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, 
with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

"""
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, 
with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


# 1st way to solving this problem.
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return nums

        x = []
        k = 0
        for i in nums:
            if i not in x:
                x.append(i)
                k += 1

        # num[:k] = x[:]
        for i in range(0, k):
            nums[i] = x[i]

        return k


# s = Solution()
# print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

# ------------------------------------------------------------


# 2nd way to solving this problem.
def sol(nums):
    x = []
    for i in nums:
        if i not in x:
            x.append(i)

    k = len(x)
    nums[:k] = x[:]

    return k, nums


# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# print(sol(nums))

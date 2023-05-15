#           Longest Common Prefix

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


# 1st way to solving this problem.
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs):
            st = strs[0]
        i = 0
        while i < len(strs):
            temp = ""
            for j in range(min(len(st), len(strs[i]))):
                if st[j] == strs[i][j]:
                    temp += st[j]
                else:
                    break
            st = temp
            i += 1
        return st


# s = Solution()
# print(s.longestCommonPrefix(["flower", "flow", "flight"]))
# ------------------------------------------------------------


# 2nd way to solving this problem.
def prefix(n):
    if len(n) == 0:
        return ""
    elif len(n) == 1:
        return n[0]
    else:
        x = n[0]

    for i in range(1, len(n)):
        st = ""
        for j in range(min(len(x), len(n[i]))):
            if x[j] == n[i][j]:
                st += x[j]
            else:
                break
        x = st
    return x


# n = ["school", "schedule", "scotland"]
# n = ["flower", "flight", "flow"]
# n = ["dog","racecar","car"]

# print(prefix(n))
# ------------------------------------


# 3rd way to solving this problem.
def Prefix2(n):
    if len(n) == 0:
        return ""
    elif len(n) == 1:
        return n[0]
    else:
        current = n[0]

    for i in range(1, len(n)):
        st = ""
        for j in range(len(n[i])):
            if j < len(current) and current[j] == n[i][j]:
                st += current[j]
            else:
                break
        current = st
    return current


# n = ["flower", "flow", "flight"]
# n = ["school", "schedule","scotland"]

# print(Prefix2(n))

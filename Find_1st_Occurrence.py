#       Find the Index of the First Occurrence in a String


"""
Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

 
Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""


def fun(a,b):

    if b in a:
        x = a.index(b)
        return x
    else:
        return -1


a = "mississippi"
b = "issip"

# print(fun(a,b))
# 28. Implement strStr() - Done 3/5/2020
# Difficulty - Easy
# https://leetcode.com/problems/implement-strstr/

# Description: Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1

print(strStr("hello", 'll'))
print(strStr("aaaaa", "bba"))

# Success - Details
# Runtime: 28 ms, faster than 75.54% of Python3 online submissions for Implement strStr().
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Implement strStr().
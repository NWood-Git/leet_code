# 344. Reverse String - Solved 2/12/2020
# Difficulty: Easy
# https://leetcode.com/problems/reverse-string/

# Instructions:
# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.

# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

def reverseString(s):
    s.reverse()

x = ["h","e","l","l","o"]
reverseString(x)
print(x)

# Not in place
# def reverseString(s):
    # return s[::-1]
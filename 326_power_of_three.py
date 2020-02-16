# 326. Power of Three - Solved 12/16/2020
# Difficulty - Easy
# https://leetcode.com/problems/power-of-three/
# Instructions:
# Given an integer, write a function to determine if it is a power of three.
# Example 1: Input: 27
# Output: true
# Example 2: Input: 0
# Output: false
# Example 3: Input: 9
# Output: true
# Example 4: Input: 45
# Output: false

# Approach with while loop
def isPowerOfThree(n):
    if n == 0:
        return False
    if n == 1:
        return True
    else:
        while n >= 3:
            n = n / 3
        if n == 1:
            return True
        else:
            return False
# Success - Details
# Runtime: 88 ms, faster than 32.82% of Python3 online submissions for Power of Three.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Power of Three.




print(isPowerOfThree(27))
print(isPowerOfThree(0))
print(isPowerOfThree(9))
print(isPowerOfThree(45))

# Approach using recursion
def isPowerOfThree_rec(n):
    if n == 1:
        return True
    elif 0 <= n < 3:
        return False
    else:
        num = n / 3
        if num == 1:
            return True
        elif num < 3:
            return False
        else:
            return isPowerOfThree_rec(num)

# print(isPowerOfThree_rec(27))
# print(isPowerOfThree_rec(0))
# print(isPowerOfThree_rec(9))
# print(isPowerOfThree_rec(45))

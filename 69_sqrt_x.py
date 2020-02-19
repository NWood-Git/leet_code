# 69. Sqrt(x) - Solved 2/19/2020
# Difficulty - Easy
# https://leetcode.com/problems/sqrtx/
# Description:
# Implement int sqrt(int x).
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
# Example 1:
# Input: 4
# Output: 2
# Example 2:
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.

def mySqrt(x):
    return int(x**.5)

print(mySqrt(4))
print(mySqrt(8))

# Success - Details
# Runtime: 32 ms, faster than 76.52% of Python3 online submissions for Sqrt(x).
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Sqrt(x).
# 137. Single Number II - Solved 2/14/2020
# Difficulty: Medium
# https://leetcode.com/problems/single-number-ii/
# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:
# Input: [2,2,3,2]
# Output: 3

# Example 2:
# Input: [0,1,0,1,0,1,99]
# Output: 99

def singleNumber(nums):
    num_set = set(nums)
    for i in num_set:
        if nums.count(i) == 1:
            return i

print(singleNumber([2,2,3,2]))
print(singleNumber([0,1,0,1,0,1,99]))

# Success - Details
# Runtime: 1360 ms, faster than 5.01% of Python3 online submissions for Single Number II.
# Memory Usage: 14.6 MB, less than 53.33% of Python3 online submissions for Single Number II.
# Next challenges: 
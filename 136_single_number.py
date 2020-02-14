# 136. Single Number - Solved 2/14/2020
# Difficulty: Easy
# https://leetcode.com/problems/single-number/
# Instructions:
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:
# Input: [2,2,1]
# Output: 1

# Example 2:
# Input: [4,1,2,1,2]
# Output: 4

def singleNumber(nums):
    num_set = set(nums)
    for i in num_set:
        if nums.count(i) == 1:
            return i

print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))

# Success - Details
# Runtime: 3676 ms, faster than 5.01% of Python3 online submissions for Single Number.
# Memory Usage: 15.2 MB, less than 9.84% of Python3 online submissions for Single Number.
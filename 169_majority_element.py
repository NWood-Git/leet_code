# 169. Majority Element - 03/02/2020
# https://leetcode.com/problems/majority-element/
# Description:
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1: Input: [3,2,3]
# Output: 3

# Example 2: Input: [2,2,1,1,1,2,2]
# Output: 2

def majorityElement(nums):
    nums_len = len(nums)
    nums_dict = {}
    
    for item in nums:
        if item in nums_dict.keys():
            nums_dict[item] += 1
            if nums_dict[item] > nums_len/2:
                return item
        else:
            nums_dict[item] = 1
            if nums_dict[item] > nums_len/2:
                return item

# print(majorityElement([2,2,1,1,1,2,2]))
# print(majorityElement([3,2,3]))
# print(majorityElement([1]))

# Success - Details
# Runtime: 192 ms, faster than 28.72% of Python3 online submissions for Majority Element.
# Memory Usage: 14.1 MB, less than 97.62% of Python3 online submissions for Majority Element.

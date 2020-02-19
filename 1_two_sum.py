# 1. Two Sum - Solved 2/18/2020
# Difficulty: Easy
# https://leetcode.com/problems/two-sum/
# Description:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(nums,target):
        k = 0
        for i in nums:
            k += 1
            if target - i in nums[k:]:
                return(k - 1, nums[k:].index(target - i) + k)

# Success - Details
# Runtime: 848 ms, faster than 25.73% of Python3 online submissions for Two Sum.
# Memory Usage: 13.7 MB, less than 83.02% of Python3 online submissions for Two Sum.

# nums = [2, 7, 11, 15]
# target = 9
nums = [3,2,4]
target = 6
print(twoSum(nums, target))



# This works for 22/29 test cases but has a runtime error - too inefficient O(n**2)?
def runtime_twoSum(nums, target):
    e_nums = list(enumerate(nums)) 
    for i in range(len(e_nums)-1):
        x = e_nums.pop(i)
        y = x[1]
        for j in e_nums:
            if y + j[1] == target:
                return [x[0],j[0]]

# nums = [2, 7, 11, 15]
# target = 9
# print(runtime_twoSum(nums, target))



#trash / scrap

# def twoSum(nums, target):
#     values = nums
#     keys = range(len(nums)-1)
#     num_dict = {k:v for (k,v) in zip(keys,values)}
#     for x in range(len(nums)-1):
#         second_num = target - nums[x]
#         z = [key for  key, value in num_dict.items() if value == second_num]
#         print(z)
#         # if len(z) >= 2 and second_num == nums[x]:
#         #     y=z[1]
#         #     return [x,y]
#         # elif len(z) == 1 and z[0] != 0 and second_num != nums[x]:
#         #     y= z[0]
#         #     return[x,y]
#         # else:
#         #     pass

# nums = [2, 7, 11, 15]
# target = 9
# nums = [3,2,4]
# target = 6
# print(twoSum(nums, target))
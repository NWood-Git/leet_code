# 283. Move Zeroes - Solved 2/19/2020
# Difficulty - Easy
# https://leetcode.com/problems/move-zeroes/
# Description
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

def moveZeroes(nums):
    x = nums.count(0)
    for i in range(x):
        nums.remove(0)
        nums.append(0)
    return nums #this is commented out in leet code, it doesn't want a return

# Success - Details
# Runtime: 96 ms, faster than 21.26% of Python3 online submissions for Move Zeroes.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Move Zeroes.

print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([0,0,1]))


def moveZeroes_2(nums):
    counter = 0
    for i in nums:
        if i == 0:
            nums.remove(0)
            nums.append(0)
        else:
            counter += 1
    return nums #this is commented out in leet code, it doesn't want a return

# Success - Details
# Runtime: 196 ms, faster than 11.49% of Python3 online submissions for Move Zeroes.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Move Zeroes.

# print(moveZeroes_2([0,1,0,3,12]))
# print(moveZeroes_2([0,0,1]))


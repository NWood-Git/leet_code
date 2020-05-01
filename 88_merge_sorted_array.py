# 88. Merge Sorted Array
# Difficulty -  Easy
# https://leetcode.com/problems/merge-sorted-array/

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as 
# one sorted array.

# Note: The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) 
# to hold additional elements from nums2.

# Example:Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]

def merge(nums1, m, nums2, n):
    """Do not return anything, modify nums1 in-place instead."""
    nums1_idx = 0
    while nums1_idx < len(nums1) and nums2:
        if nums2[0] <= nums1[nums1_idx]:
            x = nums2.pop(0)
            nums1.pop()
            nums1.insert(nums1_idx, x)
        nums1_idx += 1
    for i in nums2:
        nums1.pop()
    for i in nums2:
        nums1.append(i)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# Output: [1,2,2,3,5,6]

merge(nums1, m, nums2, n)
print(nums1)

# Success - Details 
# Runtime: 28 ms, faster than 97.14% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.9 MB, less than 6.15% of Python3 online submissions for Merge Sorted Array.

# Runtime: 36 ms, faster than 65.24% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.8 MB, less than 6.15% of Python3 online submissions for Merge Sorted Array.

# Runtime: 36 ms, faster than 65.24% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.9 MB, less than 6.15% of Python3 online submissions for Merge Sorted Array.
# Pascal's Triangle II(Recursion Card) - 119. Pascal's Triangle II
# Difficulty - Easy
# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3234/
# https://leetcode.com/problems/pascals-triangle-ii/


# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 3
# Output: [1,3,3,1]
# Follow up:

# Could you optimize your algorithm to use only O(k) extra space?


def getRow(rowIndex: int):
    if rowIndex == 0:
        desired_row = [1]
        return desired_row
    else:
        desired_row = [0] * (rowIndex+1)
        desired_row[0], desired_row[-1] = 1, 1
        if rowIndex == 1:
            return desired_row 
        else:
            prev_row = getRow(rowIndex - 1)
            for i in range(1, rowIndex):
                desired_row[i] = prev_row[i-1] + prev_row[i]
    
    return desired_row

# Submission Detail
# 34 / 34 test cases passed.
# Status: Accepted
# Runtime: 20 ms / 28 ms
# Memory Usage: 13.6 MB 
# Your runtime beats 98.49 % /  76.00 % of python3 submissions.

print(getRow(3))
print(getRow(9))
print(getRow(10))
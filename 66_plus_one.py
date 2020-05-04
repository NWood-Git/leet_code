# 66. Plus One
# Difficulty - Easy


# Description:
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1: Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2: Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

# More Optimal Solution
def plusOne(digits):
    if digits == [9]:
        return [1,0]
    idx = -1
    while digits[idx] == 9:
        digits[idx] = 0
        idx -= 1
        if idx == (len(digits) * -1):
            break
    if idx == (len(digits) * -1) and digits[idx] == 9:
        digits[0] = 0
        digits.insert(0, 1)
    else:
        digits[idx] += 1
    return digits

# Success - Details
# Runtime: 28 ms, faster than 79.22% of Python3 online submissions for Plus One.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Plus One.

# Success - Details
# Runtime: 32 ms, faster than 48.59% of Python3 online submissions for Plus One.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Plus One.

print(plusOne([1,2,3]))
print(plusOne([9,9]))
print(plusOne([2,9,9]))
print(plusOne([9]))
print(plusOne([0]))

# Inefficent solution
def plusOne_old(digits):
    new_num = int(''.join([str(num) for num in digits])) + 1
    new_digit = [int(num) for num in str(new_num)]
    return new_digit

# Success - Details
# Runtime: 32 ms, faster than 48.59% of Python3 online submissions for Plus One.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Plus One.

# Success - Details
# Runtime: 24 ms, faster than 95.05% of Python3 online submissions for Plus One.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Plus One.

# print(plusOne_old([1,2,3]))
# print(plusOne_old([2,9,9]))
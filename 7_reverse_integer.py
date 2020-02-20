# 7. Reverse Integer Done - 2/20/2020
# Difficulty - Easy
# https://leetcode.com/problems/reverse-integer/
# Description:
# Given a 32-bit signed integer, reverse digits of an integer.
# Note:
# Assume we are dealing with an environment which could only store integers within 
# the 32-bit signed integer range: [−2**31,  2**31 − 1]. For the purpose of this problem, 
# assume that your function returns 0 when the reversed integer overflows.

# Example 1: Input: 123
# Output: 321

# Example 2: Input: -123
# Output: -321

# Example 3:Input: 120
# Output: 21

def reverse(x):
    if  x < 0:
        rev_x = int(str(abs(x))[::-1]) * -1
        if rev_x >= -2**31:
            return rev_x
        else:
            return 0
    elif x >=  0:
        rev_x= int(str(x)[::-1])
    
    if  -2**31 <= rev_x <= (2**31)-1:
        return rev_x
    else:
        return 0

# Success - Details:
# Runtime: 16 ms, faster than 99.88% of Python3 online submissions for Reverse Integer.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Reverse Integer.

# def reverse(x):
#     if  x < 0:
#         rev_x = int(str(abs(x))[::-1]) * -1
#         if rev_x >= -2**31:
#             return rev_x
#         else:
#             return 0
#     elif x >=  0:
#         rev_x= int(str(x)[::-1])
#         if rev_x <= (2**31)-1:
#             return rev_x
#         else:
#             return 0
    

print(reverse(123))
print(reverse(-123))
print(reverse(120))

# y = str(123)
# x = y[::-1]
# z = str(y)[::-1]
# print(z)
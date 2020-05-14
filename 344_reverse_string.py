# 344. Reverse String - Solved 2/12/2020
# Difficulty: Easy
# https://leetcode.com/problems/reverse-string/

# Instructions:
# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.

# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


# Recursive answer 

def reverseString(s):
    def helper(l,r):
        if l < r:
            s[r], s[l] = s[l], s[r]
            helper(l+1, r-1)
    helper(0, len(s)-1)  
''' # 
class Solution:
    def helper(self,l,r,s):
            if l < r:
                s[r], s[l] = s[l], s[r]
                self.helper(l+1, r-1, s)
                
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.helper(0, len(s)-1, s)  
'''
# Success Details: 
# Runtime: 228 ms, faster than 17.42% of Python3 online submissions for Reverse String.
# Memory Usage: 38.3 MB, less than 5.81% of Python3 online submissions for Reverse String.

# Runtime: 216 ms, faster than 52.11% of Python3 online submissions for Reverse String.
# Memory Usage: 38 MB, less than 5.81% of Python3 online submissions for Reverse String.

# Not recursive
'''
def reverseString(s):
    s.reverse()
'''
x = ["h","e","l","l","o"]
reverseString(x)
print(x)

# Not in place
# def reverseString(s):
    # return s[::-1]
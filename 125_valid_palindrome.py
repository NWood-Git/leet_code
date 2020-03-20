# 125. Valid Palindrome
# Difficulty - Easy
# https://leetcode.com/problems/valid-palindrome/
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1: Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2: Input: "race a car"
# Output: false

def isPalindrome(s):
    s = ''.join(i.lower() for i in s if i.isalnum())
    idx1 = 0
    idx2 = -1
    while idx1 < len(s) // 2:
        if s[idx1] != s[idx2]:
            return False
        # print(f"idx1 = {s[idx1]} and idx2 =  {s[idx2]}")
        idx1 += 1
        idx2 -= 1
    return True

# Success - Details
# Runtime: 56 ms, faster than 28.75% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 18.7 MB, less than 5.95% of Python3 online submissions for Valid Palindrome.

# Runtime: 52 ms, faster than 44.50% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 18.8 MB, less than 5.95% of Python3 online submissions for Valid Palindrome.

print(isPalindrome("race a car"))
print(isPalindrome("racecar"))
print(isPalindrome("raceecar"))
print(isPalindrome("A man, a plan, a canal: Panama"))



def isPalindrome(s):
    s = ''.join(i.lower() for i in s if i.isalnum())
    n = len(s) // 2
    if len(s) % 2 == 0:
        first_half = s[:n]
        second_half = s[n:][::-1]
    else:
        first_half = s[:n]
        second_half = s[n+1:][::-1]
    return first_half == second_half

# Success - Details 

# Runtime: 36 ms, faster than 93.67% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 18.8 MB, less than 5.95% of Python3 online submissions for Valid Palindrome.

# Runtime: 44 ms, faster than 75.36% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 18.8 MB, less than 5.95% of Python3 online submissions for Valid Palindrome.

# Runtime: 48 ms, faster than 60.61% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 18.7 MB, less than 5.95% of Python3 online submissions for Valid Palindrome.

# print(isPalindrome1("race a car"))
# print(isPalindrome1("racecar"))
# print(isPalindrome1("raceecar"))
# print(isPalindrome1("A man, a plan, a canal: Panama"))


def isPalindrome2(s):
    s = ''.join(i.lower() for i in s if i.isalnum())
    rev_s = s[::-1]
    return s == rev_s
    
# Success - Details 

# Runtime: 48 ms, faster than 60.61% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 18.5 MB, less than 5.95% of Python3 online submissions for Valid Palindrome.

# Runtime: 48 ms, faster than 60.61% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 18.8 MB, less than 5.95% of Python3 online submissions for Valid Palindrome.

# Runtime: 44 ms, faster than 75.36% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 18.7 MB, less than 5.95% of Python3 online submissions for Valid Palindrome.

# print(isPalindrome2("race a car"))
# print(isPalindrome2("racecar"))
# print(isPalindrome2("raceecar"))
# print(isPalindrome2("A man, a plan, a canal: Panama"))
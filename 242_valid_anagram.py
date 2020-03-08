# 242. Valid Anagram - Solved 3/8/2020
# Difficulty - Easy
# https://leetcode.com/problems/valid-anagram/

# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1: Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2: Input: s = "rat", t = "car"
# Output: false

# Note: You may assume the string contains only lowercase alphabets.

# Follow up: What if the inputs contain unicode characters? How would you adapt your solution to such case?

def isAnagram(s,t):
    if len(s) != len(t):
        return False
    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True

print(isAnagram("anagram", "nagaram"))
print(isAnagram('ab', 'a'))

# Success - Details:
# Runtime: 24 ms, faster than 99.80% of Python3 online submissions for Valid Anagram.
# Memory Usage: 13.1 MB, less than 96.88% of Python3 online submissions for Valid Anagram.

# Runtime: 32 ms, faster than 97.02% of Python3 online submissions for Valid Anagram.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Valid Anagram.


def isAnagram1(s, t):
    if sorted(s) == sorted(t):
        return True
    else:
        return False

print(isAnagram1("anagram", "nagaram"))
print(isAnagram1('ab', 'a'))

# Success - Details
# Runtime: 48 ms, faster than 62.17% of Python3 online submissions for Valid Anagram.
# Memory Usage: 13.6 MB, less than 31.25% of Python3 online submissions for Valid Anagram.

def isAnagram2(s, t):
    if s == t == '':
        return True
    s_dict = {}
    for letter in s:
        if letter in s_dict.keys():
            s_dict[letter] += 1
        else:
            s_dict[letter] = 1
    
    for letter in t:
        if letter not in s_dict:
            return False
        else:
            s_dict[letter] -= 1

    for letter in s_dict:
        if s_dict[letter] != 0:
            return False
    return True

print(isAnagram2("anagram", "nagaram"))
print(isAnagram2('ab', 'a'))


# isAnagram2 is the same to slower than isAnagram1

# Success - Details
# Runtime: 52 ms, faster than 41.57% of Python3 online submissions for Valid Anagram.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Valid Anagram.
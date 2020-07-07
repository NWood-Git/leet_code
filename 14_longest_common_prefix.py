# 14. Longest Common Prefix
# Difficulty - Easy
# https://leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2: Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Note: All given inputs are in lowercase letters a-z.

def longestCommonPrefix(strs):
    result = ""
    if len(strs) == 0 or strs[0] == "":
        return result
    elif len(strs) == 1:
        return strs[0]
    
    anchor = strs[0]
    for idx in range(len(anchor)):
        for str in strs[1:]:
            try:
                str[idx]
            except IndexError:
                return result
            if str[idx] != anchor[idx]:
                return result
        result += anchor[idx]
    return result
    
# print(longestCommonPrefix(["flower","flow","flight", "f"]))
# print(longestCommonPrefix(["c","c"]))

# Success - Details 
# Runtime: 36 ms, faster than 56.71% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14.2 MB, less than 5.06% of Python3 online submissions for Longest Common Prefix.

# Runtime: 52 ms, faster than 13.28% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.9 MB, less than 53.82% of Python3 online submissions for Longest Common Prefix.

# Runtime: 36 ms, faster than 56.71% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14.1 MB, less than 22.05% of Python3 online submissions for Longest Common Prefix.
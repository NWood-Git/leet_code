# 118. Pascal's Triangle - Solved 3/8/2020
# Difficulty - Easy
# https://leetcode.com/problems/pascals-triangle/
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example: Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

def generate(numRows):
    result = [[1], [1,1]]
    if numRows == 0:
        return []
    elif numRows ==1:
        return [[1]]
    elif numRows == 2:
        return result
    else:
        for num in range(2, numRows):
            prev = result[num-1]
            new_line = [1]
            counter = 0
            for item in prev:
                if counter != len(prev) -1:
                    new_line.append(prev[counter] + prev[counter + 1])
                    counter += 1
                else:
                    new_line.append(1)
            result.append(new_line)
    return result

# Success - Details
# Runtime: 28 ms, faster than 67.42% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle.

print(generate(1))
print(generate(2))
print(generate(5))
print(generate(7))



# The below is a more efficently written version of the above code - the runtime and memory results are the same 

def generate_short(numRows):
        res = [[1 for _ in range(i+1)] for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res

# Success - Details
# Runtime: 28 ms, faster than 67.42% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle.

print(generate_short(1))
print(generate_short(2))
print(generate_short(5))
print(generate_short(7))
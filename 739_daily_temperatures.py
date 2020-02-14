# 739. Daily Temperatures - 2/11/2020
# Difficulty - Medium
# https://leetcode.com/problems/daily-temperatures/

# Instructions:
# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait 
# until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100]. 


# My Solution Below - Worked - However it is not optimal and took too long on the larger lists - NOT Accepted By Leet Code

def dailyTemperatures(T):
    wait_list = []
    counter = 1 # will inc by 1 as each value of T goes through the loop
    checker = 1 # is used to check the next warmer day within 1 iteration and is reset to 1 after each value of T goes through
    for temp in T:
        if counter == len(T):
            wait_list.append(0)
            return wait_list
        elif temp < T[counter]:
            wait_list.append(1)
        else:
            while True:
                if (counter+checker) > (len(T)-1):
                    wait_list.append(0)
                    break
                elif temp < T[counter + checker]:
                    wait_list.append(1 + checker)
                    break
                else:
                    checker += 1
        counter += 1
        checker = 1
    # return wait_list


T = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(T))


#Optimal Solution - found online
# https://www.youtube.com/watch?v=uVXjp5Qwfe8 # python (not in english)
# https://www.youtube.com/watch?v=WmwmC55hb6Q #javascript (in english)


# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         stack = []
#         result = [0 for _ in range(len(T))]
#         for i in range(len(T)):
#             while stack and T[i] > T[stack[-1]]:
#                 result[stack[-1]] = i - stack[-1]
#                 stack.pop()
#             stack.append(i)
#         return result
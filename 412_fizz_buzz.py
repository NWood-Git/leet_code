# 412. Fizz Buzz - Solved 2/13/2020
# Difficulty: Easy
# https://leetcode.com/problems/fizz-buzz/
# Instructions:
# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
# For numbers which are multiples of both three and five output “FizzBuzz”.

def fizzBuzz(n):
    result = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

print(fizzBuzz(17))


# Example:
# n = 15,
# 
# Return:
# [
    # "1",
    # "2",
    # "Fizz",
    # "4",
    # "Buzz",
    # "Fizz",
    # "7",
    # "8",
    # "Fizz",
    # "Buzz",
    # "11",
    # "Fizz",
    # "13",
    # "14",
    # "FizzBuzz"
# ]

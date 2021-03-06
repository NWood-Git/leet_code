# 121. Best Time to Buy and Sell Stock - Solved 2/13/2020
# Difficulty: Easy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Instructions:
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
# design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

# updated verion 
def maxProfit(prices):
        n = len(prices)
        if n <= 1:
                return 0
        maxprofit = 0
        low = prices[0]
        for i in range(1,n):
                low = min(low,prices[i])
                maxprofit = max(maxprofit, prices[i] - low)
        return maxprofit

# print(maxProfit([7,1,5,3,6,4]))

# Success - Details
# Runtime: 64 ms, faster than 61.89% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 13.7 MB, less than 98.85% of Python3 online submissions for Best Time to Buy and Sell Stock.


def maxProfit_old(prices):
        profit = 0
        for i in  range(len(prices)):
                mx = max(prices[i:])
                p_diff = mx - prices[i]
                if p_diff > profit:
                        profit = p_diff
        return profit

#my runtime is O(n**2) best solution is O(n)

# print(maxProfit_old([7,1,5,3,6,4]))

# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#             Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# Success - stats from leet code
# Details:
# Runtime: 5968 ms, faster than 5.34% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 13.9 MB, less than 67.82% of Python3 online submissions for Best Time to Buy and Sell Stock
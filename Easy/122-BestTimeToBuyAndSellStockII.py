# My Answer
'''
Runtime: 40 ms, faster than 76.04% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 14 MB, less than 42.31% of Python3 online submissions for Best Time to Buy and Sell Stock II.
'''
class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        if len(prices) == 0:
            return profit
        
        buyPrices = prices[:-1]
        sellPrices = prices[1:]
        for index in range(len(buyPrices)):
            if buyPrices[index] < sellPrices[index]:
                profit += sellPrices[index] - buyPrices[index]
        return profit
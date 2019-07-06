# My Answer
'''
Runtime: 48 ms, faster than 29.21% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 14.1 MB, less than 22.16% of Python3 online submissions for Best Time to Buy and Sell Stock.
'''
class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        if len(prices) == 0:
            return profit
        
        buyPoint = prices[0]
        for i in range(1, len(prices)):
            buyPoint = min(buyPoint, prices[i])
            profit = max(profit, prices[i] - buyPoint)
        return profit
    
    
# Solution
'''
Runtime: 48 ms, faster than 29.21% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 14 MB, less than 50.30% of Python3 online submissions for Best Time to Buy and Sell Stock.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/281483/2-lines-python
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from functools import reduce
        return reduce(lambda r, p: (max(r[0],p-r[1]), min(r[1],p)), prices, (0, float('inf')))[0]
    
    
    
# Solution
'''
Runtime: 40 ms, faster than 82.60% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.9 MB, less than 74.30% of Python3 online submissions for Best Time to Buy and Sell Stock.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39367/Short-python-solution-O(n)-runtime-O(1)-space

The question is simple. You want to find the difference of the maximum and the minimum. The only trick is that the bigger number should come after the smaller number.

So, here is how I tackled it. Instead of going forward, I scanned through the list of prices backward to store the current maximum number. Update the biggest difference along the way.
'''
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        length = len(prices)
        if length==0:
            return 0
        temp = prices[length-1]
        res = 0
        for i in range(length-1,-1,-1):
            temp = max(temp,prices[i])
            if temp - prices[i] > res:
                res = temp - prices[i]
        return res
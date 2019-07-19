# My Answer
'''
Runtime: 20 ms, faster than 57.32% of Python online submissions for Factorial Trailing Zeroes.
Memory Usage: 11.8 MB, less than 34.66% of Python online submissions for Factorial Trailing Zeroes.
'''
class Solution(object):
    def trailingZeroes(self, n):
        ans = 0
        while n >= 5:
            ans += n // 5
            n = n // 5
        return ans
    

# Solution
'''
Runtime: 12 ms, faster than 94.61% of Python online submissions for Factorial Trailing Zeroes.
Memory Usage: 11.9 MB, less than 5.06% of Python online submissions for Factorial Trailing Zeroes.

https://leetcode.com/problems/factorial-trailing-zeroes/discuss/337730/Python-Two-Lines-Solution.
'''
class Solution(object):
    def trailingZeroes(self, n):
        if n < 5: return 0
        return n//5 + self.trailingZeroes(n//5)
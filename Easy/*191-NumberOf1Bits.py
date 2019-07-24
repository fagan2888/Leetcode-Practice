# My Answer
'''
Runtime: 12 ms, faster than 95.07% of Python online submissions for Number of 1 Bits.
Memory Usage: 11.7 MB, less than 63.89% of Python online submissions for Number of 1 Bits.
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n > 0:
            if (n & 1):
                ans += 1
            n >>= 1
        return ans
    
    
# Solution
'''
Runtime: 12 ms, faster than 95.07% of Python online submissions for Number of 1 Bits.
Memory Usage: 11.8 MB, less than 34.96% of Python online submissions for Number of 1 Bits.

https://leetcode.com/problems/number-of-1-bits/discuss/264911/Python-O(n)-solution
'''
class Solution(object):
    def hammingWeight(self, n):
            count = 0 
            while n > 0:
                if n % 2:
                    count += 1
                n >>= 1
            return count
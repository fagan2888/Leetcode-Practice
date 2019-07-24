# My Answer
'''
Runtime: 20 ms, faster than 65.76% of Python online submissions for Reverse Bits.
Memory Usage: 11.8 MB, less than 13.31% of Python online submissions for Reverse Bits.
'''
class Solution:
    def reverseBits(self, n):
        t = 2
        ans = 0
        for length in range(31, -1, -1):
            ans += (t**length) * (n % t)
            n = n // t
        return ans
    
    
# Solution
'''
Runtime: 20 ms, faster than 65.76% of Python online submissions for Reverse Bits.
Memory Usage: 11.9 MB, less than 6.16% of Python online submissions for Reverse Bits.

https://leetcode.com/problems/reverse-bits/discuss/318099/Python-AC-solution-using-bit-operation-easy-to-understand

for more info: http://www.runoob.com/python/python-operators.html
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        shift = 31
        ans = 0
        while shift >= 0:
            ans += (n & 1) << shift
            n >>= 1
            shift -= 1
        return ans
    
    
# Solution
'''
Runtime: 16 ms, faster than 86.09% of Python online submissions for Reverse Bits.
Memory Usage: 11.8 MB, less than 40.93% of Python online submissions for Reverse Bits.

https://leetcode.com/problems/reverse-bits/discuss/55036/Very-simple-non-iterate-solution
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = ((n & 0x55555555) << 1) | ((n & 0xAAAAAAAA) >> 1)
        n = ((n & 0x33333333) << 2) | ((n & 0xCCCCCCCC) >> 2)
        n = ((n & 0x0F0F0F0F) << 4) | ((n & 0xF0F0F0F0) >> 4)
        n = ((n & 0x00FF00FF) << 8) | ((n & 0xFF00FF00) >> 8)
        n = ((n & 0x0000FFFF) << 16) | ((n & 0xFFFF0000) >> 16)
        return n
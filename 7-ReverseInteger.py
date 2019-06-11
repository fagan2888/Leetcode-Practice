# My Answer
'''
Runtime: 32 ms, faster than 97.10% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.3 MB, less than 51.60% of Python3 online submissions for Reverse Integer.
'''
class Solution:
    def reverse(self, x: int) -> int:
        pOrn = 1
        if x < 0:
            pOrn = -1
            x = abs(x)
        ans = int(str(x)[::-1]) * pOrn
        return self.check(ans)
    
    def check(self, c: int) -> int:
        if c > (2**31-1) or c < -2**31:
            return 0
        else:
            return c
# My Answer
'''
Runtime: 20 ms, faster than 78.85% of Python online submissions for Happy Number.
Memory Usage: 11.8 MB, less than 35.99% of Python online submissions for Happy Number.
'''
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n in [0, 1]:
            return bool(n)
        
        ans = 0
        for i in str(n):
            ans += int(i) ** 2

        if ans%10 == 0:
            while ans%10 == 0:
                ans = ans // 10

            if ans%2 == 0 and ans < 10:
                return False
            
        return self.isHappy(ans)
    
    
# Solution
'''
Runtime: 24 ms, faster than 55.54% of Python online submissions for Happy Number.
Memory Usage: 11.7 MB, less than 74.04% of Python online submissions for Happy Number.
'''
class Solution:
    def isHappy(self, n):
        d={}
        while True:
            nn=str(n)
            num=sum([int(x)**2 for x in nn])
            if num in d:return False
            else:d[num]=1
            if num==1:return True
            n=num
            
            
# Solution
'''
Using the fact that all unhappies go through 4 (and that 2 and 3 are unhappy)
Runtime: 24 ms, faster than 55.54% of Python online submissions for Happy Number.
Memory Usage: 11.7 MB, less than 78.66% of Python online submissions for Happy Number.

refer from: https://leetcode.com/problems/happy-number/discuss/57256/Three-short-and-easy-solutions
'''
class Solution:
    def isHappy(self, n):
        while n > 4:
            n = sum(int(d)**2 for d in str(n))
        return n == 1
    
    
'''
Tortoise and Hare algorithm
Runtime: 24 ms, faster than 55.54% of Python online submissions for Happy Number.
Memory Usage: 11.7 MB, less than 78.66% of Python online submissions for Happy Number.

refer from: https://leetcode.com/problems/happy-number/discuss/57256/Three-short-and-easy-solutions
'''
class Solution:
    def isHappy(self, n):
        s = lambda n: sum(int(d)**2 for d in str(n))
        m = s(n)
        while m != n:
            n, m = s(n), s(s(m))
        return n == 1

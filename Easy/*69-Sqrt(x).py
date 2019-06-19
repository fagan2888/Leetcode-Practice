# My Answer
'''
Runtime: 64 ms, faster than 21.34% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.3 MB, less than 30.49% of Python3 online submissions for Sqrt(x).
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 1:
            return 0
        if x == 1:
            return 1
        high, low = x, 0
        tol = 0.01
        err = 10**10
        
        while abs(err) >= tol:
            ans = (high + low) / 2
            sqrt = ans ** 2
            err = sqrt - x

            if err == 0:
                break
            elif err > 0:
                high = ans
            else:
                low = ans
        return int(ans)
          

# Solutions
def mySqrt(self, x):
    if x <= 1:
        return x 
    hi = x 
    while hi > x/hi:
        hi = (hi+x/hi)//2
    return int(hi)


def mySqrt(self, x):
    if x == 0:
        return 0
    left = 1
    right = x
    while left <= right:
        mid = (left + right) >> 1
        if mid * mid > x:
            right = mid
        elif mid * mid < x:
            if mid == left:
                return mid
            left = mid
        else:
            return mid
    return None


# applying Newton Method
'''
https://leetcode.com/problems/sqrtx/discuss/25190/Newton's-method-in-Python
https://leetcode.com/problems/sqrtx/discuss/25240/Newton-method-accepted-solution.
'''
def sqrt(self, x):
    i=1.0;
    while(True):
        j=(i+x/i)/2.0;
        if(abs(i-j)< 0.000000000005):
            break;
        i=j;
    return int(j);
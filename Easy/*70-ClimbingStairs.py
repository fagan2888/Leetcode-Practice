# My Answer
'''
Runtime: 28 ms, faster than 98.09% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.2 MB, less than 46.37% of Python3 online submissions for Climbing Stairs.
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        sol = 0
        for j, i  in enumerate(range(n, -1, -1)):
            if i >= j:
                sol += self.combination(i, j)
        return int(sol)
    
    def combination(self, i, j):
        return self.product(i) / (self.product(j) * self.product(i-j))
        
    def product(self, number):
        ans = 1
        if number == 0:
            return ans
        for n in range(1, number+1):
            ans *= n
        return ans
    

# Solution
'''
Runtime: 36 ms, faster than 75.48% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.4 MB, less than 5.11% of Python3 online submissions for Climbing Stairs.

原文：https://blog.csdn.net/coder_orz/article/details/51506414
当输入为1, 2, 3, 4, 5, 6, 7, 8, 9, 10时，观察输出为1, 2, 3, 5, 8, 13, 21, 34, 55, 89，是斐波那契数列！好了，我们找到了规律，写代码吧。
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        pre = cur = 1
        for i in range(1, n):
            pre, cur = cur, pre+cur
        return cur
    

'''
Runtime: 36 ms, faster than 75.48% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.3 MB, less than 7.87% of Python3 online submissions for Climbing Stairs.

原文：https://blog.csdn.net/coder_orz/article/details/51506414 
動態規劃
'''
class Solution(object):
    def climbStairs(self, n):
        if n == 0 or n == 1 or n == 2:
            return n
        steps = [1, 1]
        for i in range(2, n+1):
            steps.append(steps[i-1] + steps[i-2])
        return steps[n]
    
    
'''
Runtime: 36 ms, faster than 75.48% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.2 MB, less than 49.77% of Python3 online submissions for Climbing Stairs.

原文：https://leetcode.com/problems/climbing-stairs/discuss/25525/Recognizing-that-the-answer-is-equivalent-to-fibonacci(n%2B1)-Python-40ms
'''
class Solution(object):
    def __init__(self):
        self.saved = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Accurate O(1) approximation up to n=60 or so
        # return int(round((1/math.sqrt(5))*math.pow(((1+math.sqrt(5))/2),(n+1))))

        # Dynamic recursive Fibonacci solution
        # O(1) Best case (when we've solved for the same n before)
        # O(n) Worst case (when it's a new n and we haven't solved for any other n yet)
        # Average case somewhere in between, I'm not sure how to analyze it.
        if n in self.saved:
            return self.saved[n]
        else:
            if n is 0 or n is 1:
                return 1
            else:
                answer = self.climbStairs(n-1) + self.climbStairs(n-2)
                self.saved[n] = answer
                return answer
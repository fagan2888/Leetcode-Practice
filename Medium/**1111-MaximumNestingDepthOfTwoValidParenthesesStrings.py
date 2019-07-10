# Solution
'''
Runtime: 44 ms, faster than 31.28% of Python online submissions for Maximum Nesting Depth of Two Valid Parentheses Strings.
Memory Usage: 12.2 MB, less than 100.00% of Python online submissions for Maximum Nesting Depth of Two Valid Parentheses Strings.

from: 
https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/discuss/329010/Python-O(n)
'''
class Solution(object):
    def maxDepthAfterSplit(self, seq):
        stack = []
        n = len(seq)
        res = [0] * n

        for i in range(n):
            s = seq[i]
            if s == "(":
                if stack:
                    res[i] = 1 - res[stack[-1]]
                stack.append(i)
            elif s == ")":
                res[i] = res[stack[-1]]
                stack.pop()
        return res
    
    
# Solution
'''
Runtime: 36 ms, faster than 76.78% of Python online submissions for Maximum Nesting Depth of Two Valid Parentheses Strings.
Memory Usage: 12 MB, less than 100.00% of Python online submissions for Maximum Nesting Depth of Two Valid Parentheses Strings.

from contest winners~
https://leetcode.com/contest/weekly-contest-144/ranking/
'''
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        a = 0
        b = 0
        n = len(seq)
        ans = [0] * n
        
        for i, c in enumerate(seq):
            if c == '(':
                if a < b:
                    a += 1
                    ans[i] = 0
                else:
                    b += 1
                    ans[i] = 1
            else:
                if a < b:
                    b -= 1
                    ans[i] = 1
                else:
                    a -= 1
                    ans[i] = 0
        
        return ans
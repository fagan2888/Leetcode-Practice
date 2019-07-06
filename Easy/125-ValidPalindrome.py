# My Answer
'''
Runtime: 44 ms, faster than 96.28% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.5 MB, less than 26.50% of Python3 online submissions for Valid Palindrome.
'''
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) in [0, 1]:
            return True
        
        s = re.sub('[^A-Za-z0-9]+', '', s)
        s = s.lower()
        if s == s[::-1]:
            return True
        return False
        

# Solution
'''
Runtime: 52 ms, faster than 81.80% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.2 MB, less than 37.87% of Python3 online submissions for Valid Palindrome.

https://leetcode.com/problems/valid-palindrome/discuss/39982/Python-in-place-two-pointer-solution.
'''
class Solution:
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]
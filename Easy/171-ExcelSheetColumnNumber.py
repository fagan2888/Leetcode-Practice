# My Answer
'''
Runtime: 24 ms, faster than 48.82% of Python online submissions for Excel Sheet Column Number.
Memory Usage: 11.8 MB, less than 25.43% of Python online submissions for Excel Sheet Column Number.
'''
class Solution(object):
    def __init__(self):
        self.mapping = {"A": 1,"B": 2,"C": 3,"D": 4,"E": 5,"F": 6,"G": 7,"H": 8,"I": 9,"J": 10,"K": 11,"L": 12,"M": 13,"N": 14,"O": 15,"P": 16,"Q": 17,"R": 18,"S": 19,"T": 20,"U": 21,"V": 22,"W": 23,"X": 24,"Y": 25,"Z": 26}
    
    def titleToNumber(self, s):
        ans = 0
        for index, n in enumerate(s[::-1]):
            ans += self.mapping[n] * 26**(index)
        return ans
        
        
# Solution
'''
Runtime: 8 ms, faster than 99.72% of Python online submissions for Excel Sheet Column Number.
Memory Usage: 11.8 MB, less than 31.30% of Python online submissions for Excel Sheet Column Number.

https://leetcode.com/problems/excel-sheet-column-number/discuss/328334/Python-3
'''
class Solution:
    def titleToNumber(self, s):
        return sum(26**(len(s)-i-1) * (ord(c)-64) for i, c in enumerate(s))
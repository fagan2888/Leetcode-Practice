# My Answer
'''
Runtime: 12 ms, faster than 91.99% of Python online submissions for Excel Sheet Column Title.
Memory Usage: 11.8 MB, less than 41.01% of Python online submissions for Excel Sheet Column Title.
'''
class Solution(object):
    def __init__(self):
        self.mapping = {1: 'A',2: 'B',3: 'C',4: 'D',5: 'E',6: 'F',7: 'G',8: 'H',9: 'I',10: 'J',11: 'K',12: 'L',13: 'M',14: 'N',15: 'O',16: 'P',17: 'Q',18: 'R',19: 'S',20: 'T',21: 'U',22: 'V',23: 'W',24: 'X',25: 'Y',26: 'Z',0: ''}
    
    def convertToTitle(self, n):
        num1 = n // 26
        num2 = n % 26
        if num2==0 and num1==1:
            return self.mapping[26] * (num1 % 26) + self.mapping[ num1 - (num1%26) ]
        elif num1==0:
            return self.mapping[ num2 ]
        elif num1<=26 and num2==0:
            return self.mapping[num1 - 1] + self.convertToTitle(26) * (num1%26 - 1)
        elif num1>26 and num2==0:
            return self.mapping[26] * (num1//26 + num1%26) + self.convertToTitle( num2 )
        elif num1>26 and num2:
            return self.convertToTitle(num1//26) + self.convertToTitle(num1%26) + self.convertToTitle(num2)
        return self.convertToTitle( num1 ) + self.convertToTitle( num2 )
    
    
# Solution
'''
Runtime: 20 ms, faster than 53.20% of Python online submissions for Excel Sheet Column Title.
Memory Usage: 11.5 MB, less than 99.75% of Python online submissions for Excel Sheet Column Title.

https://leetcode.com/problems/excel-sheet-column-title/discuss/336155/Solution-in-Python-3-(beats-100)
'''
class Solution:
    def convertToTitle(self, n):
        s = ''
        while n > 0:
            r = n%26
            if r == 0: r = 26
            s = chr(64+r)+s
            n = int((n-r)/26)
        return(s)
    
    
'''
Runtime: 20 ms, faster than 53.20% of Python online submissions for Excel Sheet Column Title.
Memory Usage: 11.8 MB, less than 38.99% of Python online submissions for Excel Sheet Column Title.

https://leetcode.com/problems/excel-sheet-column-title/discuss/332700/Self-explainable-python-code-beats-97
'''
class Solution:
    def convertToTitle(self, n):
        alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = ''
        while n:
            res = alph[(n % 26) - 1] + res
            n = (n - 1)//26 
        return res
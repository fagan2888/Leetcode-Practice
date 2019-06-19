# My Answer
'''
Runtime: 48 ms, faster than 32.75% of Python3 online submissions for Add Binary.
Memory Usage: 13.3 MB, less than 14.12% of Python3 online submissions for Add Binary.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        acc = self.convertDecimal(a) + self.convertDecimal(b)
        return self.convertBinary(acc)
        
    def convertDecimal(self, a: str) -> int:
        acc = 0
        for exp, mul in enumerate(list(a)[::-1]):
            acc += 2 ** exp * int(mul)
        return acc
        
    def convertBinary(self, a: int) -> str:
        binary = ""
        while a > 1:
            binary += str(a % 2)
            a = a // 2
        binary += str(a % 2)
        return binary[::-1]
    
    
# Solution
'''
Runtime: 40 ms, faster than 80.34% of Python3 online submissions for Add Binary.
Memory Usage: 13.2 MB, less than 40.75% of Python3 online submissions for Add Binary.
'''
class Solution:
    def addBinary(self, a, b):
        if len(a)==0: return b
        if len(b)==0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + str(int(a[-1]) + int(b[-1]))
        
        
# Solution
'''
Runtime: 40 ms, faster than 80.34% of Python3 online submissions for Add Binary.
Memory Usage: 13.3 MB, less than 21.71% of Python3 online submissions for Add Binary.
'''
class Solution:
    def addBinary(self, a, b):
        return '{:b}'.format(int(a,2)+int(b,2))
    
    
# Solution
'''
Runtime: 44 ms, faster than 61.03% of Python3 online submissions for Add Binary.
Memory Usage: 13.2 MB, less than 36.45% of Python3 online submissions for Add Binary.
'''
class Solution:
    def addBinary(self, a, b):
        i, j, carry, res = len(a)-1, len(b)-1, 0, ""
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            res = str(carry%2) + res
            carry //= 2
        return res
    
    
    
# Solution
'''
Runtime: 36 ms, faster than 94.25% of Python3 online submissions for Add Binary.
Memory Usage: 13 MB, less than 88.27% of Python3 online submissions for Add Binary.
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # hashmap of truth table
        m = {
                    ('0','0','0'): ('0','0'),
                    ('0','0','1'): ('0','1'),
                    ('0','1','0'): ('0','1'),
                    ('0','1','1'): ('1','0'),
                    ('1','0','0'): ('0','1'),
                    ('1','0','1'): ('1','0'),
                    ('1','1','0'): ('1','0'),
                    ('1','1','1'): ('1','1'),
                }
        # initialize return str
        r = ''
        
        # eqalize the length of strings
        # "11", "1" will become "11", "01"
        if len(a) > len(b):
            b = '0'*(len(a)-len(b)) + b
        elif len(a) < len(b):
            a = '0'*(len(b)-len(a)) + a

        # Initial MSB, LSB is 0, 0
        t = ('0','0')
        for i in range(1,len(a)+1):
            t = m[t[0],a[-i],b[-i]]
            r = t[1] + r
        
        # if MSB is not 0, we have a carry and we need to add it
        if '0' not in t[0]:
            r = t[0] + r
        
        return r
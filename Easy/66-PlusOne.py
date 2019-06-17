# My Answer
'''
Runtime: 52 ms, faster than 12.64% of Python3 online submissions for Plus One.
Memory Usage: 13.1 MB, less than 70.47% of Python3 online submissions for Plus One.
'''
class Solution:
    def plusOne(self, digits):
        acc = 0
        for exp, mul in enumerate(digits[::-1]):
            acc += 10**exp * mul
        acc = acc + 1
        return [int(i) for i in list(str(acc))]
    
    
    
# Solution
'''
Runtime: 36 ms, faster than 85.71% of Python3 online submissions for Plus One.
Memory Usage: 13.1 MB, less than 68.22% of Python3 online submissions for Plus One.
'''
class Solution:
    def plusOne(self, digits):
        return [int(x) for x in str(int(''.join([str(x) for x in digits])) + 1)]
    
    
# Solution
'''
Runtime: 28 ms, faster than 99.27% of Python3 online submissions for Plus One.
Memory Usage: 13.2 MB, less than 52.03% of Python3 online submissions for Plus One.
'''
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)
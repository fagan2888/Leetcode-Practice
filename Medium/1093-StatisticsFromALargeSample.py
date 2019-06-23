# My Answer
'''
Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Statistics from a Large Sample.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Statistics from a Large Sample.
'''
import random
class Solution:
    def sampleStats(self, count):
        for k in count:
            if k != 0:
                minimum = float(count.index(k))
                break
        
        
        countRe = list(reversed(count))
        for k in countRe:
            if k != 0:
                maximum = len(count) - countRe.index(k) - 1.0
                break
        
        
        summary = 0
        for integer, k in enumerate(count):
            summary += integer*k
        mean = round(summary / sum(count), 5)
        
        
        totalNum = sum(count)
        half = totalNum // 2
        if totalNum % 2 == 0:
            med1, med2 = half-1, half
        else:
            med1 = med2 = half
            
        current = 0
        getMed1, getMed2 = True, True
        for integer, k in enumerate(count):
            current += k 
            if current > med1 and getMed1:
                med1 = integer
                getMed1 = False
            if current > med2 and getMed2:
                med2 = integer
                getMed2 = False
                
            if not (getMed1 or getMed2):
                break
        median = (med1 + med2) / 2
        
        
        maxSample = max(count)
        mode = float(count.index(maxSample))
        
        return [
            minimum, maximum, mean, median, mode
        ]
    

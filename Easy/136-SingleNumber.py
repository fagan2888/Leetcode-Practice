# My Answer
'''
Runtime: 36 ms, faster than 95.12% of Python3 online submissions for Single Number.
Memory Usage: 14.9 MB, less than 49.21% of Python3 online submissions for Single Number.
'''
class Solution:
    def singleNumber(self, nums) -> int:
        ansDict = {}
        for n in nums:
            if n not in ansDict.keys():
                ansDict[n] = 1
            else:
                del ansDict[n]
        return list(ansDict.keys())[0]
    
    
# Solution
'''
Runtime: 32 ms, faster than 98.91% of Python3 online submissions for Single Number.
Memory Usage: 14.7 MB, less than 74.60% of Python3 online submissions for Single Number.

https://leetcode.com/problems/single-number/discuss/321912/Python-Solution(just-xor-operation)

Python Solution(just xor operation)
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            ans ^= x
        return ans
    
'''
https://leetcode.com/problems/single-number/discuss/43000/Python-different-solutions.
'''
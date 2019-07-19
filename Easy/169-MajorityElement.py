# My Answer
'''
Runtime: 160 ms, faster than 43.27% of Python online submissions for Majority Element.
Memory Usage: 13.3 MB, less than 59.92% of Python online submissions for Majority Element.
'''
class Solution(object):
    def majorityElement(self, nums):
        mapping = {}
        for n in nums:
            if mapping.get(n) is not None:
                mapping[n] += 1
                continue
            mapping[n] = 1
            
        return max(mapping.items(), key=lambda s: s[1])[0]
        

# Solution
'''
Runtime: 136 ms, faster than 99.35% of Python online submissions for Majority Element.
Memory Usage: 13.3 MB, less than 75.83% of Python online submissions for Majority Element.

https://leetcode.com/problems/majority-element/discuss/51770/Three-line-Python-solution
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = list(nums)
        l.sort()
        return l[len(l)/2]
    
'''
https://leetcode.com/problems/majority-element/discuss/51712/Python-different-solutions-(dictionary-bit-manipulation-sorting-divide-and-conquer-brute-force-etc).
'''
# My Answer
'''
Runtime: 16 ms, faster than 83.51% of Python online submissions for House Robber.
Memory Usage: 11.8 MB, less than 37.72% of Python online submissions for House Robber.

learn from: https://www.cnblogs.com/grandyang/p/4383632.html
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        ans = [nums[0], max(nums[:2])]
        for index in range(len(nums)):
            if index < 2:
                continue
            ans.append(max(nums[index] + ans[-2], ans[-1]))
        return ans[-1]
    
    
'''
Runtime: 16 ms, faster than 83.51% of Python online submissions for House Robber.
Memory Usage: 11.8 MB, less than 34.83% of Python online submissions for House Robber.
'''
class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        robOdd = robEven = 0
        for index, n in enumerate(nums):
            if index % 2 == 1:
                robOdd += n
                robOdd = max(robOdd, robEven)
            else:
                robEven += n
                robEven = max(robOdd, robEven)
            print(robOdd, robEven)
        return max(robOdd, robEven)
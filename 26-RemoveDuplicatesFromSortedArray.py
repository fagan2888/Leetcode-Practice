# My Answer
'''
Runtime: 56 ms, faster than 92.79% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 14.8 MB, less than 47.75% of Python3 online submissions for Remove Duplicates from Sorted Array.
'''
class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums)==0:
            return 0
        
        acc = 0
        for ind in range(1, len(nums)):
            if nums[ind] != nums[acc]:
                nums[acc+1] = nums[ind]
                acc += 1
        return acc+1, nums
    
    

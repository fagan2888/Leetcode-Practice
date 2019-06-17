# My Answer
'''
Runtime: 36 ms, faster than 85.57% of Python3 online submissions for Search Insert Position.
Memory Usage: 13.6 MB, less than 85.90% of Python3 online submissions for Search Insert Position.
'''
class Solution:
    def searchInsert(self, nums, target) -> int:
        pointer = 0
        for n in nums:
            if n < target:
                pointer += 1
            else:
                break
        return pointer
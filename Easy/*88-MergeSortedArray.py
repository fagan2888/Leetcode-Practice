# My Answer
'''
Runtime: 40 ms, faster than 77.67% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13.1 MB, less than 85.43% of Python3 online submissions for Merge Sorted Array.
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        pointer = 0
        while index < len(nums1) and pointer < len(nums2):
            if nums1[index] >= nums2[pointer]:
                nums1.insert(index, nums2[pointer])
                pointer += 1
            index += 1
        
        index = m + pointer
        while pointer < len(nums2):
            nums1.insert(index, nums2[pointer])
            pointer += 1
            index += 1
            
            
        nums1[:] = nums1[:(m+n)]
        


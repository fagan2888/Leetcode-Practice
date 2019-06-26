# My Answer
'''
Runtime: 64 ms, faster than 79.49% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.4 MB, less than 86.60% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        midpoint = len(nums) // 2
        ans = TreeNode(nums[midpoint])
        ans.left = self.sortedArrayToBST(nums[ :midpoint ])
        ans.right = self.sortedArrayToBST(nums[ (midpoint+1): ])
        return ans
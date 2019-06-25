# My Answer
'''
Runtime: 52 ms, faster than 41.81% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.2 MB, less than 83.42% of Python3 online submissions for Maximum Depth of Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        if not isinstance(root, TreeNode):
            return 1
        
        depth = 1
        return depth + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    
# Solution
'''
Runtime: 44 ms, faster than 92.75% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 14.6 MB, less than 87.19% of Python3 online submissions for Maximum Depth of Binary Tree.

https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
'''
class Solution(object):
    def maxDepth(self, root):
        # use BFS with iterative 
        # BFS + deque   
        if not root:
            return 0
        queue = collections.deque([(root, 1)]) # here the 2nd number is level
        while queue:
            curr, val = queue.popleft()
            if curr.left:
                queue.append((curr.left, val+1))
            if curr.right:
                queue.append((curr.right, val+1))
        return val
    


# My Answer
'''
Runtime: 40 ms, faster than 89.31% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 13.4 MB, less than 48.72% of Python3 online submissions for Binary Tree Level Order Traversal II.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        ans = []
        queue = [(root, 0)]
        while len(queue) > 0:
            root, level = queue.pop()
            
            if not root:
                continue
            elif isinstance(root, int):
                element = root
            else:
                element = root.val
                queue.insert(0, (root.left, level+1))
                queue.insert(0, (root.right, level+1))
            
            if len(ans) <= level:
                ans.insert(level, [element])
            else:
                ans[level] = ans[level] + [element]
        return ans[::-1]
    
    

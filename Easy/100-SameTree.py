# My Answer
'''
Runtime: 36 ms, faster than 80.91% of Python3 online submissions for Same Tree.
Memory Usage: 13.2 MB, less than 42.65% of Python3 online submissions for Same Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if self.unfoldTreeNode(p) == self.unfoldTreeNode(q):
            return True
        return False
    
    def unfoldTreeNode(self, p):
        if isinstance(p, (int, float)) or p is None:
            return p
        return [p.val, self.unfoldTreeNode(p.left), self.unfoldTreeNode(p.right)]
        

# Solution
'''
Runtime: 36 ms, faster than 80.91% of Python3 online submissions for Same Tree.
Memory Usage: 13 MB, less than 93.36% of Python3 online submissions for Same Tree.

using the concept of Recursion
'''
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)
    
    
'''
Runtime: 28 ms, faster than 98.70% of Python3 online submissions for Same Tree.
Memory Usage: 13.1 MB, less than 79.30% of Python3 online submissions for Same Tree.

using the concept of Iteration
'''
from collections import deque
class Solution:
    def isSameTree(self, p, q):
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p, q),])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
                    
        return True
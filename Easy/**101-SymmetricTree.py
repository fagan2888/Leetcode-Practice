# Solution
'''
Runtime: 32 ms, faster than 98.43% of Python3 online submissions for Symmetric Tree.
Memory Usage: 13.2 MB, less than 57.86% of Python3 online submissions for Symmetric Tree.

https://leetcode.com/problems/symmetric-tree/discuss/33325/Python-short-recursive-solution.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, l, r):
        if l and r:
            return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
        return l == r


'''
Runtime: 36 ms, faster than 93.31% of Python3 online submissions for Symmetric Tree.
Memory Usage: 13.1 MB, less than 76.26% of Python3 online submissions for Symmetric Tree.

https://leetcode.com/problems/symmetric-tree/discuss/33068/6line-AC-python
'''
class Solution:
    def isSymmetric(self, root) -> bool:
        def isSym(L,R):
            if not L and not R: return True
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        if root is None:
            return True
        return isSym(root.left, root.right)


'''
Runtime: 48 ms, faster than 20.89% of Python3 online submissions for Symmetric Tree.
Memory Usage: 13.4 MB, less than 8.61% of Python3 online submissions for Symmetric Tree.

原文：https://blog.csdn.net/coder_orz/article/details/51579528
'''
class Solution:
    def isSymmetric(self, root) -> bool:
        if root is None:
            return True
        return self.symmetric(root.left, root.right)
        
    def symmetric(self, left, right):
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
    
        return self.symmetric(left.left, right.right) and self.symmetric(left.right, right.left)

    
'''
Runtime: 40 ms, faster than 81.08% of Python3 online submissions for Symmetric Tree.
Memory Usage: 13.2 MB, less than 57.86% of Python3 online submissions for Symmetric Tree.

原文：https://blog.csdn.net/coder_orz/article/details/51579528
'''
class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        stackl, stackr = [root.left], [root.right]
        while len(stackl) > 0 and len(stackr) > 0:
            left = stackl.pop()
            right = stackr.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            if left.val != right.val:
                return False
            stackl.append(left.left)
            stackl.append(left.right)
            stackr.append(right.right)
            stackr.append(right.left)
        return len(stackl) == 0 and len(stackr) == 0

    
'''
Runtime: 36 ms, faster than 93.31% of Python3 online submissions for Symmetric Tree.
Memory Usage: 13.3 MB, less than 12.67% of Python3 online submissions for Symmetric Tree.

原文：https://blog.csdn.net/coder_orz/article/details/51579528
'''
class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        queuel, queuer = [root.left], [root.right]
        while len(queuel) > 0 and len(queuer) > 0:
            left = queuel.pop()
            right = queuer.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            if left.val != right.val:
                return False
            queuel.insert(0, left.left)
            queuel.insert(0, left.right)
            queuer.insert(0, right.right)
            queuer.insert(0, right.left)
        return len(queuel) == 0 and len(queuer) == 0

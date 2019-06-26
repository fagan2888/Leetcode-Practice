# My Answer
'''
Runtime: 76 ms, faster than 34.02% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 17.7 MB, less than 94.27% of Python3 online submissions for Balanced Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        if abs(self.TreeDepth(root.left) - self.TreeDepth(root.right)) < 2:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
        
    def TreeDepth(self, root):
        if not root:
            return 0
        if not isinstance(root, TreeNode):
            return 1
        
        return max(self.TreeDepth(root.left), self.TreeDepth(root.right)) + 1
    
    
# Solution
'''
Runtime: 84 ms, faster than 13.95% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 17.8 MB, less than 91.98% of Python3 online submissions for Balanced Binary Tree.

为了避免节点高度的重复计算，可利用TreeNode节点结构中的val保存每个节点的高度（或用额外的字典保存），求出所有节点高度后，用思路一的方法，DFS递归判断是否是平衡二叉树。
原文：https://blog.csdn.net/coder_orz/article/details/51335758
'''
class Solution(object):
    def isBalanced(self, root):
        if root == None:
            return True

        self.getAllDepth(root)

        left_depth = root.left.val if root.left else 0
        right_depth = root.right.val if root.right else 0
        if abs(left_depth - right_depth) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def getAllDepth(self, root):
        if root == None:
            return 0
        root.val = 1 + max(self.getAllDepth(root.left), self.getAllDepth(root.right))
        return root.val
    
    
    
# **** Solution
'''
Runtime: 52 ms, faster than 95.80% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 17.7 MB, less than 96.46% of Python3 online submissions for Balanced Binary Tree.

在思路一和思路二的基础上，考虑一遍DFS，在求出每个节点高度的同时，判断是否是平衡二叉树。 
理论上说，对每个节点的访问应该返回两个值：是否平衡、节点高度，为了节省空间，若用-1表示不平衡的状态则可省去一个变量。
原文：https://blog.csdn.net/coder_orz/article/details/51335758
'''
class Solution(object):
    def isBalanced(self, root):
        return self.dfs(root) != -1

    def dfs(self, root):
        if root == None:
            return True

        left_depth = self.dfs(root.left)
        if left_depth == -1:
            return -1
        right_depth = self.dfs(root.right)
        if right_depth == -1:
            return -1

        return 1 + max(left_depth, right_depth) if abs(left_depth - right_depth) <= 1 else -1

# My Solution
'''
Runtime: 52 ms, faster than 8.07% of Python online submissions for Minimum Depth of Binary Tree.
Memory Usage: 14.7 MB, less than 47.47% of Python online submissions for Minimum Depth of Binary Tree.
'''
class Solution(object):
    def minDepth(self, root, fir=True):
        if not root and fir:
            return 0
        if not root:
            return float("inf")
            
        if isinstance(root.val, int) and not (root.left or root.right):
            return 1
        
        return 1 + min(self.minDepth(root.left, fir=False), self.minDepth(root.right, fir=False))


    
# Solution
'''
Runtime: 36 ms, faster than 62.27% of Python online submissions for Minimum Depth of Binary Tree.
Memory Usage: 14.7 MB, less than 54.17% of Python online submissions for Minimum Depth of Binary Tree.

from https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/36094/My-solution-in-python
'''
class Solution:
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left==None or root.right==None:
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.right),self.minDepth(root.left))+1
    
    
# Solution
'''
Runtime: 44 ms, faster than 16.36% of Python online submissions for Minimum Depth of Binary Tree.
Memory Usage: 14.6 MB, less than 61.83% of Python online submissions for Minimum Depth of Binary Tree.

from https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/272579/4-Lines-Simplest-Python-Easy-to-Understand-DFS

when min(l, r) is 0, which means the leftchild or rightchild of node is not exist, then return the max(l, r) which is length of another branch.
'''
class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        return (min(l, r) or max(l, r)) +1
    
    
# Solution
'''
Runtime: 28 ms, faster than 94.57% of Python online submissions for Minimum Depth of Binary Tree.
Memory Usage: 14.6 MB, less than 60.60% of Python online submissions for Minimum Depth of Binary Tree.

from https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/269742/My-solution-using-BFS-(python)

Once I find that this node is a lead node, I can directly return current depth, which is exactly the result
'''
from collections import deque
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        
        queue = deque([root])
        depth = 1
        
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth
        
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            depth += 1
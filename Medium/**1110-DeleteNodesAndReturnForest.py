# Solution
'''
Runtime: 52 ms, faster than 63.41% of Python online submissions for Delete Nodes And Return Forest.
Memory Usage: 12.2 MB, less than 100.00% of Python online submissions for Delete Nodes And Return Forest.

from contest winners~
'''
class Solution(object):
    def dfs(self, root, detached):
        if not root:
            return
        if detached and root.val not in self.x:
            self.ans.append(root)
            
        detached = (root.val in self.x)
        self.dfs(root.left, detached)
        self.dfs(root.right, detached)
        
        # delete the value in to_delete from root
        if root.left and root.left.val in self.x:
            root.left = None
        if root.right and root.right.val in self.x:
            root.right = None
        if root.val in self.x:
            del root
        
    
    def delNodes(self, root, to_delete):
        self.x = set(to_delete)
        self.ans = []
        self.dfs(root, detached=True)
        return self.ans
# My Answer
'''
Runtime: 96 ms, faster than 6.14% of Python online submissions for Lowest Common Ancestor of Deepest Leaves.
Memory Usage: 12.4 MB, less than 100.00% of Python online submissions for Lowest Common Ancestor of Deepest Leaves.
'''
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root 
        
        leaves = self.getDeepest(root)
        if len(leaves) == 1:
            return leaves[0][0]
        
        maxParent = (root, 0)
        queue = [(root, 0)]
        while len(queue) > 0:
            curr, depth = queue.pop()
            
            if not curr:
                continue
            if all(self.checkChild(curr, l[0]) for l in leaves):
                if maxParent[1] < depth:
                    maxParent = (curr, depth)
            
            queue.append((curr.left, depth+1))
            queue.append((curr.right, depth+1))
        return maxParent[0]
        
    def checkChild(self, root, baby):
        if not root or not baby:
            return False
        
        if root is baby:
            return True
        
        return False or self.checkChild(root.right, baby) or self.checkChild(root.left, baby)
    
    def getDeepest(self, root):
        if not root:
            return root
        
        ans = []
        queue = [(root, 0)]
        while len(queue) > 0:
            
            curr, depth = queue.pop()
            if not curr:
                continue
                
            if not (curr.right or curr.left):
                ans.append((curr, depth))
                continue
            
            queue.append( (curr.right, depth + 1) )
            queue.append( (curr.left, depth + 1) )

        maxDepth = max(ans, key=lambda x:x[1])
        ans = [i for i in ans if i[1] == maxDepth[1]]
        return ans
    
    
# Solution
'''
Runtime: 40 ms, faster than 58.28% of Python online submissions for Lowest Common Ancestor of Deepest Leaves.
Memory Usage: 12.2 MB, less than 100.00% of Python online submissions for Lowest Common Ancestor of Deepest Leaves.

https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/discuss/334577/JavaC%2B%2BPython-Two-Recursive-Solution

Solution 1: Get Subtree Height and LCA
helper function return the subtree height and lca and at the same time.
null node will return depth 0,
leaves will return depth 1.
'''
class Solution(object):
    def lcaDeepestLeaves(self, root):
        def helper(root):
            if not root: return 0, None
            h1, lca1 = helper(root.left)
            h2, lca2 = helper(root.right)
            if h1 > h2: return h1 + 1, lca1
            if h1 < h2: return h2 + 1, lca2
            return h1 + 1, root
        return helper(root)[1]
    
'''
Runtime: 28 ms, faster than 99.08% of Python online submissions for Lowest Common Ancestor of Deepest Leaves.
Memory Usage: 12.2 MB, less than 100.00% of Python online submissions for Lowest Common Ancestor of Deepest Leaves.

https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/discuss/334577/JavaC%2B%2BPython-Two-Recursive-Solution

Solution 2: Get Subtree Deepest Depth
helper function return the deepest depth of descendants.
deepest represent the deepest depth.
We use a global variable lca to represent the result.
One pass, Time O(N) Space O(H)
'''
class Solution(object):
    def lcaDeepestLeaves(self, root):
        self.lca, self.deepest = None, 0
        def helper(node, depth):
            self.deepest = max(self.deepest, depth)
            if not node:
                return depth
            left = helper(node.left, depth + 1)
            right = helper(node.right, depth + 1)
            if left == right == self.deepest:
                self.lca = node
            return max(left, right)
        helper(root, 0)
        return self.lca
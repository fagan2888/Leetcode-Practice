# My Answer
'''
Runtime: 48 ms, faster than 83.62% of Python3 online submissions for Path Sum.
Memory Usage: 15.3 MB, less than 32.42% of Python3 online submissions for Path Sum.
'''
class Solution:
    def hasPathSum(self, root: TreeNode, summary: int) -> bool:
        if not root:
            return False
        
        queue = [(root, summary)]
        while len(queue) > 0:
            curr = queue.pop()
            
            if not curr[0]:
                continue
            if not curr[0].right and not curr[0].left:
                if curr[1] == curr[0].val:
                    return True
                continue
            
            queue.append((curr[0].left, curr[1] - curr[0].val))
            queue.append((curr[0].right, curr[1] - curr[0].val))
        return False
    
    
    
# Solution
'''
Runtime: 64 ms, faster than 12.90% of Python3 online submissions for Path Sum.
Memory Usage: 15.4 MB, less than 5.30% of Python3 online submissions for Path Sum.

https://leetcode.com/problems/path-sum/discuss/36360/Short-Python-recursive-solution-O(n)
'''
class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True
        
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
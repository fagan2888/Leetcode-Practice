# My Answer
'''
Runtime: 232 ms, faster than 100.00% of Python3 online submissions for Path In Zigzag Labelled Binary Tree.
Memory Usage: 46.1 MB, less than 100.00% of Python3 online submissions for Path In Zigzag Labelled Binary Tree.
'''
import math
class Solution:
    def pathInZigZagTree(self, label):
        maxDepth = int(math.log2(label))
        starter = 1
        ans = []
        
        for level in range(maxDepth, 0, -1):
            
            order = label % 2**level
            levelList = list(range(2**level, 2**(level+1)))            
            levelList = levelList[::starter]
            
            ans.append(levelList[order])
            label = label // 2
            starter *= -1
            
        ans.append(1)
        return ans[::-1]
    
    
# Solution
'''
Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Path In Zigzag Labelled Binary Tree.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Path In Zigzag Labelled Binary Tree.

https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/323310/Python-1-Line-Solution
'''
def pathInZigZagTree(self, x):
    return self.pathInZigZagTree(3 * 2 ** (len(bin(x)) - 4) - 1 - int(x / 2)) + [x] if x > 1 else [1]


# Solution
'''
Runtime: 28 ms, faster than 100.00% of Python3 online submissions for Path In Zigzag Labelled Binary Tree.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Path In Zigzag Labelled Binary Tree.

https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/323349/More-math-than-coding
'''
def pathInZigZagTree(self, label: int) -> List[int]:
    level = math.floor((math.log(label+ 0.5,2)))
    ans = [label] * (level+1)
    while level > 0:
        if level % 2 == 1:
            ans[level-1] = (2**(level+1) - ans[level] + 2**level - 1) // 2
        else:
            ans[level-1] = 2**(level) - (ans[level] // 2 - 2**(level-1) + 1)
        level -= 1
    return ans


# Solution
'''
Runtime: 20 ms, faster than 100.00% of Python3 online submissions for Path In Zigzag Labelled Binary Tree.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Path In Zigzag Labelled Binary Tree.

https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/323381/My-simple-Python-solution
'''
import math
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        if label == 1:
            return [1]
        if label == 2:
            return [1,2]
        if label == 3:
            return [1,3]
        
        m = math.floor(math.log(label)/float(math.log(2)))
        A = int(math.ceil(2**m - label*0.5)+2**(m-1)-1)
        
        outA = self.pathInZigZagTree(A)
        out = outA 
        out.append(int(label))
        return out
# My Answer
'''
Runtime: 40 ms, faster than 23.35% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13 MB, less than 89.92% of Python3 online submissions for Pascal's Triangle II.
'''
class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex == 0:
            return [1]
        ansList = [1 for _ in range(rowIndex//2 + 1)]
        for i in range(len(ansList)):
            ansList[i] = int(self.product(rowIndex) / (self.product(rowIndex - i) * self.product(i)))
                
        if (rowIndex % 2) == 0:
            ansList = ansList + ansList[::-1][1:]
        else:
            ansList = ansList + ansList[::-1]
        return ansList
    
    def product(self, k):
        if k == 0:
            return 1
        result = 1
        for i in range(1, k+1):
            result *= i
        return result
    
    
# Solution
'''
Runtime: 40 ms, faster than 23.35% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.3 MB, less than 10.92% of Python3 online submissions for Pascal's Triangle II.

https://leetcode.com/problems/pascals-triangle-ii/discuss/38565/4-lines-pythonic-easy-solution-O(k)-space-40ms
'''
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(rowIndex):
            row = [u+v for u, v in zip(row+[0], [0]+row)]
        return row
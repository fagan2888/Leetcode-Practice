# My Answer
'''
Runtime: 36 ms, faster than 75.00% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.3 MB, less than 9.68% of Python3 online submissions for Pascal's Triangle.
'''
class Solution:
    def generate(self, numRows: int):
        ansList = []
        for n in range(numRows):
            row = []
            for k in range(n // 2 + 1):
                row.append(self.combination(n, k))
            
            if (n % 2) == 0:
                row = row + row[::-1][1:]
            else:
                row = row + row[::-1]
            
            ansList.append(row)
        return ansList
        
    def combination(self, n, k):
        return int(self.product(n) / (self.product(k) * self.product(n-k)))
    
    def product(self, k):
        if k == 0:
            k = 1
        
        result = 1
        for i in range(1, k+1):
            result *= i
        return result
        
#     Time Limit Exceeded Error
#     def combination(self, n, k):
#         if k == 0 or n==k:
#             return 1
#         return self.combination(n-1, k-1) + self.combination(n-1, k)


# Solution
'''
Runtime: 32 ms, faster than 91.70% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.3 MB, less than 18.26% of Python3 online submissions for Pascal's Triangle.
'''
class Solution:
    def generate(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle
    
    
    
# Solution
'''
Runtime: 24 ms, faster than 99.82% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.3 MB, less than 7.77% of Python3 online submissions for Pascal's Triangle.

https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map.
explanation: Any row can be constructed using the offset sum of the previous row. Example:

    1 3 3 1 0 
 +  0 1 3 3 1
 =  1 4 6 4 1
'''
class Solution:
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res.append(list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])))
        return res[:numRows]
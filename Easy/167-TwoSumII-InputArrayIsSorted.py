# My Answer
'''
Runtime: 68 ms, faster than 12.35% of Python online submissions for Two Sum II - Input array is sorted.
Memory Usage: 12.8 MB, less than 5.10% of Python online submissions for Two Sum II - Input array is sorted.
'''
class Solution(object):
    def twoSum(self, numbers, target):
        mapping = {}
        for k, v in enumerate(numbers):
            if mapping.get(target - v) is not None:
                mapping[target - v].append(k + 1)
            else:
                mapping[target - v] = [k + 1]
                
        for remain, ind1 in mapping.items():
            for ind2, n in enumerate(numbers[ind1[0]:]):
                if n == remain:
                    return ind1[0], ind1[0] + ind2 + 1
                
                
# Solution
'''
Runtime: 48 ms, faster than 80.37% of Python online submissions for Two Sum II - Input array is sorted.
Memory Usage: 12 MB, less than 58.24% of Python online submissions for Two Sum II - Input array is sorted.

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/326426/EASY-PYTHON-CODE-or-Two-pointers
'''
class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
        return [0, 0] 
    
    
# Solution
'''
Runtime: 48 ms, faster than 80.37% of Python online submissions for Two Sum II - Input array is sorted.
Memory Usage: 12 MB, less than 54.71% of Python online submissions for Two Sum II - Input array is sorted.

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51249/Python-different-solutions-(two-pointer-dictionary-binary-search).
'''
class Solution(object):
    def twoSum(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i
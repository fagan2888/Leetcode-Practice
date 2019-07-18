# My Answer
'''
Runtime: 28 ms, faster than 43.23% of Python online submissions for Relative Sort Array.
Memory Usage: 12 MB, less than 100.00% of Python online submissions for Relative Sort Array.
'''
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        if len(arr1) == 0:
            return arr1
        if len(arr2) == 0:
            return sorted(arr1)
        
        mapping = {value: 0 for value in arr2}
        for a in arr1:
            if a in mapping.keys():
                mapping[a] += 1
            else:
                mapping[a] = 1
        
        ansList = []
        for b in arr2:
            ansList.extend( [b] * mapping[b] )
        
        for remain in sorted(list(set(mapping.keys()) - set(arr2))):
            ansList.extend( [remain] * mapping[remain] )
            
        return ansList
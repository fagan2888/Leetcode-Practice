# My Answer
'''
Runtime: 36 ms, faster than 80.46% of Python3 online submissions for Length of Last Word.
Memory Usage: 13.2 MB, less than 67.96% of Python3 online submissions for Length of Last Word.
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        splitList = s.split(" ")
        splitList = [x for x in splitList if x]
        
        if len(splitList) == 0:
            return 0
        return len(splitList[-1])
    

# Solution
'''
Runtime: 32 ms, faster than 93.26% of Python3 online submissions for Length of Last Word.
Memory Usage: 13.2 MB, less than 67.96% of Python3 online submissions for Length of Last Word.
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip(" ").split(" ")[-1])
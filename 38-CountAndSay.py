# My Answer
'''
Runtime: 40 ms, faster than 84.05% of Python3 online submissions for Count and Say.
Memory Usage: 13.2 MB, less than 44.07% of Python3 online submissions for Count and Say.
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        for i in range(1, n+1):
            if i == 1:
                current = "1"
            else:
                current = self.say(self.count(current))
        return current
    
    def count(self, s):
        current = s[0]
        acc = 1
        ans = []
        for subStr in s[1:]:
            if subStr != current:
                ans.append((current, acc))
                current = subStr
                acc = 1
            else:
                acc += 1

        ans.append((current, acc))
        return ans
    
    
    def say(self, tupList):
        return "".join([str(acc) + num for num, acc in tupList])
# My Answer
'''
Runtime: 60 ms, faster than 100.00% of Python3 online submissions for Distribute Candies to People.
Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Distribute Candies to People.
'''
class Solution:
    def distributeCandies(self, candies, num_people):
        ans = [0] * num_people
        n = int((-1 + math.sqrt(1+8*candies)) / 2)
        nList = list(range(1, n+1))
        ansIndex = 0
        for index in range(len(nList)):
            ans[ansIndex] = ans[ansIndex] + nList[index]
            ansIndex += 1
            if ansIndex == len(ans):
                ansIndex = 0
        
        ans[ansIndex] = ans[ansIndex] + int(candies - n*(n+1)/2)
        return ans
    
    
# Solution
'''
Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Distribute Candies to People.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Distribute Candies to People.

https://leetcode.com/problems/distribute-candies-to-people/discuss/323364/JavaC%2B%2BPython-O(sqrt(candies))-with-explanation
'''
class Solution:
    def distributeCandies(self, candies, n):
        res = [0] * n
        i = 0
        while candies > 0:
            res[i % n] += min(candies, i + 1)
            candies -= i + 1
            i += 1
        return res
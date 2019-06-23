# My Answer
'''
Runtime: 248 ms, faster than 100.00% of Python3 online submissions for Car Pooling.
Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Car Pooling.
'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxTrip = max(trips, key=lambda x: x[2])[2]
        checking = dict.fromkeys(list(range(1, maxTrip+1)), 0)
        for t in trips:
            
            for loc in range(t[1], t[2]):
                checking[loc] += t[0]
        
        if max(checking.values()) > capacity:
            return False
        return True
    
    
    
# Solution
'''
Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Car Pooling.
Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Car Pooling.
'''
class Solution(object):
    def carPooling(self, trips, capacity):
        t = [0 for _ in range(1001)]
        for n, s, e in trips:
            t[s] += n
            t[e] -= n
        cur = 0
        for i in range(1001):
            cur += t[i]
            if cur > capacity:
                return False
        return True
    
    

'''
Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Car Pooling.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Car Pooling.
'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dic = {}
        people_in_car = 0

        for num, start, end in trips:
            dic[start] = dic.get(start, 0) + num
            dic[end] = dic.get(end, 0) - num

        for stop in sorted(dic):
            people_in_car += dic[stop]
            if people_in_car > capacity:
                return False

        return True
# Solution
'''
Runtime: 832 ms, faster than 36.39% of Python online submissions for Corporate Flight Bookings.
Memory Usage: 25.6 MB, less than 100.00% of Python online submissions for Corporate Flight Bookings.

from contest winners~
'''
class Solution:
    def corpFlightBookings(self, bookings, n):
        a = [0] * n
        for i, j, k in bookings:
            # 把起始日期 +k，結束日期 -k
            a[i - 1] += k
            if j < n:
                a[j] -= k
                
        seats = 0
        for i in range(n):
            # 累加每個日期
            seats += a[i]
            a[i] = seats
        return a
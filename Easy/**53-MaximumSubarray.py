# 需要使用 "動態規劃"

# My Answer
'''
1st Submission: Time Limit Exceeded
'''
from itertools import combinations
class Solution:
    def maxSubArray(self, nums) -> int:
        ans = max(nums)
        for start, end in combinations(range(len(nums)+1), 2):
            if nums[start] > 0:
                ans = max( ans, sum(nums[start:end]) )
        return ans
                

'''
reference from https://blog.csdn.net/fuxuemingzhu/article/details/71101802
Runtime: 44 ms, faster than 79.99% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.8 MB, less than 38.04% of Python3 online submissions for Maximum Subarray.
'''
class Solution:
    def maxSubArray(self, nums) -> int:
        ans = float("-inf")
        current, previous = 0, 0
        for index in range(len(nums)):
            # if previous value less than zero, 
            # than not adding previous value, current equals to itself
            current = nums[index] + (previous if previous>0 else 0)

            # choose maximum value from current and ans
            ans = max(ans, current)

            # replace previous with current, 
            # so previous will always be the maximum value of previous combination
            previous = current
        return ans    
    
'''
reference from https://blog.csdn.net/zl87758539/article/details/51676108
Runtime: 44 ms, faster than 79.99% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.7 MB, less than 41.75% of Python3 online submissions for Maximum Subarray.
'''
class Solution:
    def maxSubArray(self, nums) -> int:
        l, g = float("-inf"), float("-inf")
        for n in nums:
            l = max(n, n+l)
            g = max(g, l)
        return g
    
    
    
'''
reference from https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/
'''
# A Divide and Conquer based program 
# for maximum subarray sum problem 
  
# Find the maximum possible sum in 
# arr[] auch that arr[m] is part of it 
def maxCrossingSum(arr, l, m, h) : 
      
    # Include elements on left of mid. 
    sm = 0; left_sum = -10000
      
    for i in range(m, l-1, -1) : 
        sm = sm + arr[i] 
          
        if (sm > left_sum) : 
            left_sum = sm 
      
      
    # Include elements on right of mid 
    sm = 0; right_sum = -1000
    for i in range(m + 1, h + 1) : 
        sm = sm + arr[i] 
          
        if (sm > right_sum) : 
            right_sum = sm 
      
  
    # Return sum of elements on left and right of mid 
    return left_sum + right_sum; 
  
  
# Returns sum of maxium sum subarray in aa[l..h] 
def maxSubArraySum(arr, l, h) : 
      
    # Base Case: Only one element 
    if (l == h) : 
        return arr[l] 
  
    # Find middle point 
    m = (l + h) // 2
  
    # Return maximum of following three possible cases 
    # a) Maximum subarray sum in left half 
    # b) Maximum subarray sum in right half 
    # c) Maximum subarray sum such that the  
    #     subarray crosses the midpoint  
    return max(maxSubArraySum(arr, l, m), 
               maxSubArraySum(arr, m+1, h), 
               maxCrossingSum(arr, l, m, h)) 
              
  
# Driver Code 
arr = [2, 3, 4, 5, 7] 
n = len(arr) 
  
max_sum = maxSubArraySum(arr, 0, n-1) 
print("Maximum contiguous sum is ", max_sum) 
  
# This code is contributed by Nikita Tiwari. 
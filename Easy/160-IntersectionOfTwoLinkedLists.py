# My Answer
'''
Runtime: 196 ms, faster than 69.20% of Python online submissions for Intersection of Two Linked Lists.
Memory Usage: 41.7 MB, less than 92.45% of Python online submissions for Intersection of Two Linked Lists.
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        x, xList = headA, []
        y, yList = headB, []
        while x or y:
            if x is y:
                break
                
            if x:
                xList.append(x)
                x = x.next
            if y:
                yList.append(y)
                y = y.next
        
        if x is y:
            if len(xList) == 0 and len(yList) == 0:
                return x
            
            while x is y:
                if len(xList) == 0 or len(yList) == 0:
                    return x
                x = xList.pop()
                y = yList.pop()
            return x.next
        return None
    
    
    
# Solution
'''
Runtime: 188 ms, faster than 87.79% of Python online submissions for Intersection of Two Linked Lists.
Memory Usage: 41.9 MB, less than 34.61% of Python online submissions for Intersection of Two Linked Lists.

https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments

the idea is if you switch head, the possible difference between length would be countered. 
On the second traversal, they either hit or miss. 
if they meet, pa or pb would be the node we are looking for, 
if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None
'''
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None
    

'''
Runtime: 220 ms, faster than 17.82% of Python online submissions for Intersection of Two Linked Lists.
Memory Usage: 41.9 MB, less than 31.92% of Python online submissions for Intersection of Two Linked Lists.

https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments
'''
class Solution(object):
    def getIntersectionNode(self, A, B):
        if not A or not B: return None

        # Concatenate A and B
        last = A
        while last.next: last = last.next
        last.next = B

        # Find the start of the loop
        fast = slow = A
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                fast = A
                while fast != slow:
                    slow, fast = slow.next, fast.next
                last.next = None
                return slow

        # No loop found
        last.next = None
        return None
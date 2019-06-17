# My Solution
'''
Runtime: 40 ms, faster than 92.34% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.3 MB, less than 25.04% of Python3 online submissions for Merge Two Sorted Lists.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val == [] and l2.val == []:
            return None
        
        ans = self.getValue(l1) + self.getValue(l2)
        ans = sorted(ans)
        ansListNode = self.fromList(ans)
        return ansListNode
        
    def fromList(self, l):
        if len(l) == 0:
            return ListNode(None)
        
        item = ListNode(l[-1])
        for i in l[::-1][1:]:
            nextTmp = ListNode(i)
            nextTmp.next = item
            item = nextTmp
        return item
    
    def getValue(self, item):
        if item.val in [[], None]:
            return []
        
        end = [item.val]
        noneNode = item.next
        while noneNode is not None:
            end.append(noneNode.val)
            noneNode = noneNode.next
        return end
    
    
    
# Solution
'''
Runtime: 44 ms, faster than 79.71% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.1 MB, less than 78.35% of Python3 online submissions for Merge Two Sorted Lists.
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
'''
Runtime: 36 ms, faster than 97.85% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.1 MB, less than 80.17% of Python3 online submissions for Merge Two Sorted Lists.
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        head = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return head.next
# My Answer
'''
Runtime: 44 ms, faster than 91.68% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.3 MB, less than 10.01% of Python3 online submissions for Remove Duplicates from Sorted List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        ansList = [head.val]
        while (head is not None):
            if ansList[-1] != head.val:
                ansList.append(head.val)
            head = head.next
            
        ans = None
        for num in ansList[::-1]:
            tmp = ListNode(num)
            tmp.next = ans
            ans = tmp
        
        return ans
    
    
    
# Solution
'''
Runtime: 40 ms, faster than 98.03% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.2 MB, less than 31.77% of Python3 online submissions for Remove Duplicates from Sorted List.

原文：https://leetcode.com/problems/remove-duplicates-from-sorted-list/discuss/28874/Accepted-Python-code
使用兩個pointer
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = curr = head
        while curr:
            if pre.val != curr.val:
                pre.next = curr
                pre = curr
            else:
                pre.next = curr.next
            curr = curr.next
        return head
    
    
'''
Runtime: 48 ms, faster than 79.17% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.3 MB, less than 21.64% of Python3 online submissions for Remove Duplicates from Sorted List.

原文：https://leetcode.com/problems/remove-duplicates-from-sorted-list/discuss/235167/python-28ms
'''
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
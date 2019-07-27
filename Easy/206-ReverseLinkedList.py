# My Answer
'''
Runtime: 20 ms, faster than 88.19% of Python online submissions for Reverse Linked List.
Memory Usage: 15.5 MB, less than 22.84% of Python online submissions for Reverse Linked List.
'''
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        ans = None
        while head.next:
            tmp = ListNode(head.val)
            tmp.next = ans
            ans = tmp
            head = head.next
        finalAns = ListNode(head.val)
        finalAns.next = ans
        return finalAns
    
# Solution:
'''
from: https://leetcode.com/problems/reverse-linked-list/discuss/319396/Python-iteratively-and-recursively
Iteratively with runtime O(n), extra space O(1).

Runtime: 20 ms, faster than 88.19% of Python online submissions for Reverse Linked List.
Memory Usage: 13.6 MB, less than 72.31% of Python online submissions for Reverse Linked List.
'''
def reverseList(self, head: ListNode) -> ListNode:
    reverse = None
    ptr = head
    while ptr:
        reverse, reverse.next, ptr = ptr, reverse, ptr.next
    return reverse

'''
from: https://leetcode.com/problems/reverse-linked-list/discuss/319396/Python-iteratively-and-recursively
Recursively with runtime O(n), extra space O(n) as we need stack when doing recursion

Runtime: 24 ms, faster than 67.75% of Python online submissions for Reverse Linked List.
Memory Usage: 17.3 MB, less than 11.05% of Python online submissions for Reverse Linked List.
'''
def reverseList(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    N = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return N    
# Solution
'''
https://stackoverflow.com/questions/20353835/fastest-way-to-prove-linked-list-is-circular-in-python

Runtime: 40 ms, faster than 75.95% of Python online submissions for Linked List Cycle.
Memory Usage: 18.2 MB, less than 30.98% of Python online submissions for Linked List Cycle.

A good algorithm is as follows, it may very well be the best. You do not need to copy the list or anything, like that, it can be done in constant space.

Take two pointers and set them to the beginning of the list.

Let one increment one node at a time and the other two nodes at a time.

If there is a loop at any point in the list, they will have to be pointing to the same node at some point (not including the starting point). Obviously if you reach the end of the list, there is no loop.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        
        slow = head
        fast = head

        while fast != None:
            slow = slow.next

            if fast.next != None:
                fast = fast.next.next
            else:
                return False

            if slow is fast:
                return True
        return False
__author__ = 'WangZhe'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head

        while head is not None and head.val == val:
            head = head.next
        if head is None:
            return head
        else:
            last = head
            this = head.next
            while this is not None:
                if this.val == val:
                    last.next = this.next
                    this = this.next
                else:
                    this = this.next
                    last = last.next
            return head
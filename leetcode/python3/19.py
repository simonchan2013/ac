# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = 1
        tmp = head
        while tmp.next:
            l = l + 1
            tmp = tmp.next
            
        tarIdx = l - n - 1
        if tarIdx < 0:
            return head.next
        
        
        curr = head
        i = 0
        while i < tarIdx:
            curr = curr.next
            i = i + 1

        curr.next = curr.next.next
        
        return head

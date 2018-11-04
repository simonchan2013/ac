# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1Len = 1
        l2Len = 1
        tmp = l1
        while tmp.next:
            l1Len += 1
            tmp = tmp.next
            
        tmp = l2
        while tmp.next:
            l2Len += 1
            tmp = tmp.next
            
        lCurr = l1
        sCurr = l2
        result = l1
        if l2Len > l1Len:
            lCurr = l2
            sCurr = l1
            result = l2
        
        base = 0
        prev = lCurr
        while lCurr is not None:
            sCurrValue = sCurr.val if sCurr is not None else 0
            tmpValue = base + lCurr.val + sCurrValue
            base = tmpValue // 10
            lCurr.val = tmpValue % 10
            
            prev = lCurr
            lCurr = lCurr.next
            if sCurr is not None:
                sCurr = sCurr.next
                
        if base == 1:
            prev.next = ListNode(1)
            
        return result

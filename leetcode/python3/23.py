# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        d = {}
        for l in lists:
            while l is not None:
                if d.get(l.val) is None:
                    d[l.val] = 1
                else:
                    d[l.val] += 1
                    
                l = l.next
                    
        ll = list(d.keys())
        ll.sort()
        
        tarHead = None
        tar = None
        for i in range(len(ll)):
            for j in range(d[ll[i]]):
                if tar is None:
                    tar = ListNode(ll[i])
                    tarHead = tar
                else:
                    tar.next = ListNode(ll[i])
                    tar = tar.next
            
        return tarHead

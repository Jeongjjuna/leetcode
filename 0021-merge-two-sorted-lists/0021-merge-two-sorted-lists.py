# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = list1
        p2 = list2
        
        
        start = ListNode(-101, None)
        n = start
        while p1 != None and p2 != None:
            # p1, p2중에서 더 작은 숫자를 연결한다.
            if p1.val <= p2.val:
                n.next = p1
                next = p1.next
                n = p1
                p1 = next
            else:
                n.next = p2
                next = p2.next
                n = p2
                p2 = next
        
        if p1 == None:
            n.next = p2
        else:
            n.next = p1
            
        return start.next
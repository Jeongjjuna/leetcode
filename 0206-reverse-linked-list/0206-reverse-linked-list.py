# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        n = head
        prev = None
        
        while n != None:
            next = n.next
            n.next = prev
            prev = n
            n = next
        
        return prev
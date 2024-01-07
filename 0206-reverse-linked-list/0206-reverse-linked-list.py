# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque


class Solution:
    
    # 접근1. 연결리스트를 앞에서부터 탐색하며 거꾸로 연결하기
    # 시간복잡도 : O(n)
    def sol_1(self, head):
        n = head
        prev = None
        
        while n != None:
            next = n.next
            n.next = prev
            prev = n
            n = next
            
        return prev
    
    
    # 접근2. deque로 변환하기 O(n)
    def sol_2(self, head):
        if head == None:
            return head
        
        dq = deque()
        # dq에 순차적으로 집어넣기
        node = head
        while node != None:
            dq.append(node)
            node = node.next
        
        # 뒤에서부터 재연결해주기
        for i in range(len(dq) - 1, 0, -1):
            dq[i].next = dq[i - 1]
        dq[0].next = None
        
        return dq[len(dq) - 1]
        
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.sol_2(head)
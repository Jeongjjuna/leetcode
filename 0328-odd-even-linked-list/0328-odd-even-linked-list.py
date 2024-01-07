# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        
        
        
        start_p1 = head # 짝수시작 0
        start_p2 = head.next # 홀수시작 1
        
        p1 = start_p1# 짝수 node를 나타낸다.
        p2 = start_p2# 홀수 node를 나타낸다.
        
        
        node = head
        cnt = 0 # 짝수/홀수 구별 카운트
        while node != None:
            if node == start_p1 or node == start_p2:
                node = node.next
                cnt += 1
                continue
                
            
            # 짝수라면
            if cnt % 2 == 0:
                p1.next = node
                p1 = node
                
            # 홀수라면
            else:
                p2.next = node
                p2 = node
            
            node = node.next
            cnt += 1
        
        if p1 != None:
            p1.next = None
        if p2 != None:
            p2.next = None
        # 최종적으로 짝수 끝노드가, 홀수 첫 노드를 가르킨다.
        p1.next = start_p2
        
        return start_p1
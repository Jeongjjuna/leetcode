/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import java.util.*;

class Solution {
    public boolean isPalindrome(ListNode head) {
        
        // 1. 연결리스트의 int값들을 deque배열에 순차적으로 담는다.
        Deque<Integer> deque = new ArrayDeque<>();

        ListNode node = head;
        while (node != null) {
            deque.add(node.val);
            node = node.next;
        }

        // 2. deque의 맨앞과 맨뒤의 값을 비교하면서 팰린드롬을 판별한다.
        node = head;
        while (!deque.isEmpty()) {
           if(deque.removeLast() != node.val) {
               return false;
           }
            node = node.next; 
        }
        return true;  
    }  
}

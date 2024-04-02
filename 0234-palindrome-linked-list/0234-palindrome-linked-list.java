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
        Deque<Integer> stack = new ArrayDeque<>();

        ListNode node = head;
        while (node != null) {
            stack.add(node.val);
            node = node.next;
        }

        node = head;
        
        // System.out.println(stack);
        // System.out.println(node.val);

        while (!stack.isEmpty()) {
            //int a = stack.pop();
            //int b = node.val;
            //System.out.println(a);
            //System.out.println(b);

           if(stack.removeLast() != node.val) {
               //System.out.println("이거 왜 출력 안됨?");
               return false;
           }
            // if (!stack.pop().equals(node.val)) { 
           //      return false; 
           //  }
            node = node.next; 
        }
        return true;  
    }  
}

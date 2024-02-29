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
class Solution {
    private int len(ListNode pntr){
        int ans = 0;
        if(pntr == null){
            return 0;
        }
        while(pntr != null){
            pntr = pntr.next;
            ans += 1;
        }
        return ans;
    }
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode pntr1 = head;
        ListNode pntr2 = head;

        int trv = len(head) - n;
        if(trv == 0) return head.next;
        while(trv > 1){
            head = head.next;
            trv -= 1;
        }
        if(head.next == null){
            return head.next;
        }
        
        head.next = head.next.next;
        return pntr1;
    }
}

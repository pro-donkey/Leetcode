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
    private int len(ListNode head){
        int cnt = 0;
        while(head!= null){
            
            cnt += 1;
            head = head.next;

        }
        return cnt;
    }
    public ListNode deleteMiddle(ListNode head) {
        ListNode head2 = head;
        int sz = len(head);
        if(sz == 0 || sz == 1){
            return null;
        }
        for(int i=0;i<(sz/2)-1;i++){
            head = head.next;
        }
        head.next = head.next.next;

        return head2;
    }
}

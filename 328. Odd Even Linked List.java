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
    public ListNode oddEvenList(ListNode head) {
        ListNode odd = new ListNode(-1);
        ListNode even = new ListNode(-1);
        ListNode odd1 = odd;
        ListNode even1 = even;
        ListNode odd3 = odd;
        ListNode head2 = head;
        int cnt = 1;
        while(head2!= null){
            if(cnt %2 != 0){
                odd.next = new ListNode(head2.val);
                odd = odd.next;
            }
            else {
                even.next = new ListNode(head2.val);
                even = even.next;
            }
            head2 = head2.next;
            cnt += 1;
        }
        while(odd3.next != null){
            odd3 = odd3.next;
        }
        odd3.next = even1.next;

        return odd1.next;
    }
}

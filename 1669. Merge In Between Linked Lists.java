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
        public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode l1 = list1;
        ListNode l2;
        for (int i = 0; i < a - 1; i++) {
            l1 = l1.next;
        }
        l2 = l1;
        for (int i = a - 1; i < b; i++) {
            l2 = l2.next;
        }
        while (list2 != null) {
            l1.next = list2;
            l1 = l1.next;
            list2 = list2.next;
        }
        l1.next = l2.next;
        return list1;
    }
}

// Brute Force
// T.C O(n log n) because we used sorting


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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Brute Force Approch
        ArrayList<Integer> arr = new ArrayList<>();
        ListNode h1 = list1;
        ListNode h2 = list2;

        while(h1 != null){
            int data = h1.val;
            arr.add(data);
            h1 = h1.next;
        }
        while(h2 != null){
            int data = h2.val;
            arr.add(data);
            h2 = h2.next;
        }

        Collections.sort(arr);
        ListNode ans = new ListNode(-1);
        ListNode head = ans;
        for(int i=0;i<arr.size();i++){
            head.next = new ListNode(arr.get(i));
            head = head.next;
        }
        return ans.next;
    }
}

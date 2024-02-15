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
    public int pairSum(ListNode head) {
        ArrayList<Integer> arr = new ArrayList<>();
        ListNode head2 = head;
        while(head2!= null){
            arr.add(head2.val);
            head2 = head2.next;
        }
        int max = Integer.MIN_VALUE;
        for(int i=0;i<arr.size()/2;i++){
            int sum = arr.get(i) + arr.get(arr.size()-i-1);
            max = Math.max(max,sum);
        }
        return max;
    }
}




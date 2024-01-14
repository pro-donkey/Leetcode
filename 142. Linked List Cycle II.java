/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        HashSet<ListNode> set = new HashSet<>();
        while(slow != null){
            if(set.contains(slow)){
                fast = slow;
                return fast;
            }
            else{
                set.add(slow);
            }
            slow = slow.next;
            
        }

        return null;
    }
}

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
    public ListNode mergeKLists(ListNode[] lists) {
        int size = lists.length;
        if(size == 0) return null;
        ArrayList<Integer> arr = new ArrayList<>();
        for(ListNode it : lists){
            ListNode pnt = it;
            while(pnt != null){
                arr.add(pnt.val);
                pnt = pnt.next;
            }
        }

        Collections.sort(arr);
        ListNode ans = new ListNode(-1);
        ListNode val = ans;
        for(Integer it: arr){
            ans.next = new ListNode(it);
            ans = ans.next;
        }

        return val.next;
    }
}

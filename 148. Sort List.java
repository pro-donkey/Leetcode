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

    public ListNode middle(ListNode head)
    {
        ListNode slow =head;
        ListNode fast =head;
        while(fast.next!=null&&fast.next.next!=null)
        {
            slow=slow.next;
            fast=fast.next.next;
        }
        return slow;  

    }
    public ListNode merge(ListNode left,ListNode right)
    {
        ListNode dummy=new ListNode(0);
        ListNode temp=dummy;
        while(left!=null&&right!=null)
        {
            if(left.val<right.val)
            {
                temp.next=left;
                left=left.next;
                temp=temp.next;
            }
            else
            {
                temp.next=right;
                right=right.next;
                temp=temp.next;
            }
        }
        if(left!=null)
        {
            temp.next=left;
        }
        if(right!=null)
        {
            temp.next=right;
        }
        return dummy.next;
    }
    public ListNode sortList(ListNode head) 
    {
        if(head==null||head.next==null)
        {
            return head;
        }
        ListNode mid=middle(head);
        ListNode left=head;
        ListNode right=mid.next;
        mid.next=null;

        return merge(sortList(left),sortList(right));
        
    }
}

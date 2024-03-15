# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1 = ""
        st2 = ""
        while l1 != None:
            st1 += str(l1.val)
            l1 = l1.next
        
        while l2 != None:
            st2 += str(l2.val)
            l2 = l2.next
        
        ans = int(st1[::-1]) + int(st2[::-1])
        ans = str(ans)
        ans = ans[::-1]
        head = ListNode(-1)
        head2 = head
        for i in ans:
            head.next = ListNode(i)
            head = head.next
        return head2.next
        

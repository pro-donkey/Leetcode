# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return True
        
        s = ""
        while head!= None:
            s += str(head.val)
            head = head.next
        
        if s == s[::-1]:
            return True
        
        return False

        

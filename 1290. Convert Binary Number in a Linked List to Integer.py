# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = []
        while head != None:
            ans.append(str(head.val))
            head = head.next 
        
        s = ''.join(ans) 

        return int(s,2)

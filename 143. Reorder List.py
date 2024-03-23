# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pnt1 = head
        pnt2 = head
        pnt3 = head

        arr = []
        while pnt2:
            arr.append(pnt2.val)
            pnt2 = pnt2.next
        left ,right = 0, len(arr)-1
        while left <= right:
            pnt1.val = arr[left]
            pnt1 = pnt1.next
            if pnt1 != None :
                pnt1.val = arr[right]
                pnt1 = pnt1.next
            left +=1
            right -= 1



# optimized solution 

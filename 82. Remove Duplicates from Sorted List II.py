# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Extreme Brute Force 
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        mp = {}
        while head:
            if head.val in mp:
                mp[head.val] += 1
            else:
                mp[head.val] = 1
            head = head.next

        for key, value in list(mp.items()):
            if value > 1:
                del mp[key]

        if len(mp) == 0:
            return None
        arr = []
        for key in mp:
            arr.append(key)
        arr.sort()
        ans = ListNode(arr[0])
        pos = ans
        for i in range(1, len(arr)):
            ans.next = ListNode(arr[i])
            ans = ans.next

        return pos



# Most common solution 
class Solution(object):
    def deleteDuplicates(self, head):
        dummy_head = ListNode(-1)
        dummy_head.next = head
        current, previous = head, dummy_head
        while current:
            while current.next and current.val == current.next.val:
                current = current.next
            
            if previous.next == current:
                previous = previous.next
                current = current.next
            else:
                previous.next = current.next
                current = previous.next
        return dummy_head.next


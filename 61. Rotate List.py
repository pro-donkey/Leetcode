class Solution:
    def reverse(self, arr: List[int], start: int, end: int) -> None:
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def rotate(self, arr: List[int], k: int) -> None:
        n = len(arr)
        k = k % n
        self.reverse(arr, 0, n - k - 1)
        self.reverse(arr, n - k, n - 1)
        self.reverse(arr, 0, n - 1)

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next

        self.rotate(vals, k)

        dummy = ListNode(-1)
        current = dummy
        for val in vals:
            current.next = ListNode(val)
            current = current.next

        return dummy.next

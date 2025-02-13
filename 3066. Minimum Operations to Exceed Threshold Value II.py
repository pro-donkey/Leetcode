import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        pq = []
        heapq.heapify(pq)
        for val in nums:
            heapq.heappush(pq, val)

        cnt = 0
        while pq and pq[0] < k:
            val1 = heapq.heappop(pq)
            if not pq: 
                return cnt
            val2 = heapq.heappop(pq)
            new = min(val1, val2) * 2 + max(val1, val2)
            heapq.heappush(pq, new)
            cnt += 1

        return cnt

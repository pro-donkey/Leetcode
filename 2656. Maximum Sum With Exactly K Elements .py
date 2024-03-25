import sys 

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        mx = float('-inf')
        for num in nums:
            mx = max(num, mx)
        ans = 0
        while k > 0:
            ans += mx + k-1
            k -= 1
        return ans

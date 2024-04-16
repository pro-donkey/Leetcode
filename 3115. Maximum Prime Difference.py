from typing import List

class Solution:
    def check(self, n: int) -> bool:
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        else:
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        mn = float("inf")
        mx = float("-inf")
        for i in range(len(nums)):
            if self.check(nums[i]):
                mn = min(mn, i)
                mx = max(mx, i)

        ans = abs(mx - mn)
        return ans

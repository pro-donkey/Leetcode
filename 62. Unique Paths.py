import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = m + n - 2
        comb = n - 1
        ans = math.comb(total, comb)

        return ans

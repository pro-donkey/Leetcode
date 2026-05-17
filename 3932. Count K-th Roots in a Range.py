import math


class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        if k == 1:
            return r - l + 1
        low = math.ceil(l ** (1 / k))
        high = round(r ** (1 / k))

        cnt = 0

        for i in range(low, high + 1):
            ans = i**k
            if l <= ans <= r:
                cnt += 1

        return cnt

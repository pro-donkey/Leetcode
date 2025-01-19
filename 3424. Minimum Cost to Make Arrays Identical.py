class Solution:
    def calculate_abs_diff(self, arr: List[int], brr: List[int]) -> int:
        n = len(arr)
        df = 0
        for i in range(n):
            df += abs(arr[i] - brr[i])

        return df

    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:

        ans = self.calculate_abs_diff(arr, brr)

        arr.sort()
        brr.sort()

        ans = min(ans, self.calculate_abs_diff(arr, brr) + k)

        return ans

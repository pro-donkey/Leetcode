class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:

        mx = 0
        n = len(nums)
        for i in range(1, n):
            diff = abs(nums[i] - nums[i - 1])
            mx = max(mx, diff)

        mx = max(mx, abs(nums[-1] - nums[0]))
        return mx

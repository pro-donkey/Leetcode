class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        n = len(nums)
        prod = 1
        for right in range(n):
            prod *= nums[right]
            while prod >= k and left <= right:
                prod /= nums[left]
                left += 1
            
            ans += right - left + 1

        return ans




# using dynamic sliding window algo

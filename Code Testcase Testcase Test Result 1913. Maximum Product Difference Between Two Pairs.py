class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        pr1 = nums[n-2]*nums[n-1]
        pr2 = nums[0]*nums[1]

        return pr1 - pr2

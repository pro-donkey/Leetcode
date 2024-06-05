class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndx = 0
        for i in range(len(nums)):
            if i > maxIndx:
                return False
            maxIndx = max(maxIndx, i + nums[i])
            if maxIndx >= len(nums):
                return True

        return True

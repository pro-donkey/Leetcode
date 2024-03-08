class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        mn = nums[0]
        mx = nums[n-1]
        cnt = 0
        for i in range(1,n-1):
            if nums[i] < mx and nums[i] > mn:
                cnt += 1
        
        return cnt
        

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        ans = 0
        pre = 0
        mp = {0:1}
        for num in nums:
            pre += num
            ans += mp.get(pre-goal,0)
            mp[pre] = mp.get(pre,0) + 1
        
        return ans


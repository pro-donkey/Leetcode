class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        pre = 0
        mp = {0:1}
        for num in nums:
            pre += num
            ans += mp.get(pre-k,0)
            mp[pre] = mp.get(pre,0) + 1
        
        return ans


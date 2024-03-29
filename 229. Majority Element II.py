class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = {}
        n = len(nums)
        for i in nums:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
        ans = []
        mx_val = n // 3
        for key, val in mp.items():
            if val > mx_val:
                ans.append(key)
        return ans

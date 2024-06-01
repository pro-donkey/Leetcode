class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mp = Counter(nums)
        ans = []
        for key ,val in mp.items():
            if val == 1:
                ans.append(key)
        
        return ans

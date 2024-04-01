class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = list(set(permutations(nums)))
        return ans

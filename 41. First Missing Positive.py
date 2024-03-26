class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        st = set(nums)
        for i in range(1,n+2):
            if i not in st:
                return i
            

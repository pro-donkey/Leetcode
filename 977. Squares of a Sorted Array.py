class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [num**2 for num in nums]
        ans = sorted(ans)
        return ans
        

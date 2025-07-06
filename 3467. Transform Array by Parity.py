class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even = odd = 0
        for val in nums:
            if val % 2:
                odd += 1
            else:
                even += 1
        
        arr = [0]*even + [1]*odd
        return arr 

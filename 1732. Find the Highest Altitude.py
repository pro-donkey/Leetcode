class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = 0
        pre = 0
        for num in gain:
            pre += num 
            mx = max(pre,mx)
        return mx
        
        

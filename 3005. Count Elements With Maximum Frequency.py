class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mp = {}
        for i in nums:
            if i in mp:
                mp[i] += 1
            
            else :
                mp[i] = 1
        
        mx = 0
        for val in mp.values():
            if val >= mx:
                mx = val
        
        sm = 0
        for val in mp.values():
            if val == mx:
                sm += mx
        
        return sm
        

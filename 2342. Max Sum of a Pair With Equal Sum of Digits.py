class Solution:
    def convert_sm(self,val :int)->int:
        sm = 0
        while val > 0:
            sm += val % 10
            val = val // 10 

        return sm 
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        sm_arr = [self.convert_sm(val) for val in nums]
        mp = defaultdict(list)
        for i in range(n):
            mp[sm_arr[i]].append(nums[i])
        
        sm = 0
        mx = 0
        for val in mp.values():
            if len(val) > 1:
                val.sort()
                sm = val[-1] + val[-2]
            
            mx = max(mx,sm)
        
        return -1 if mx == 0 else mx

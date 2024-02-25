class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        st1 = set()
        st2 = set()
        cnt = 1
        for i in nums:
            if cnt % 2 == 0:
                st2.add(i)
            else :
                st1.add(i)
            
            cnt += 1
        
        if len(st1) == (len(nums)/2) and len(st2) == (len(nums)/2):
            return True
        return False
        

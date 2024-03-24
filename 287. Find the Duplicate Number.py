class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sett = set()
        for num in nums:
            if num in sett:
                return num
            else :
                sett.add(num)
        
        return -1
        

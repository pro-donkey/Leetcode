class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        sett = set()
        ans = []
        for num in nums:
            if num in sett:
                ans.append(num)
            else :
                sett.add(num)
        
        return ans

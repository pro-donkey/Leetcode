class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        pnt1 = 0
        pnt2 = 0
        n = len(nums1)
        m = len(nums2)

        while pnt1 < n  and pnt2 < m:
            if nums1[pnt1] < nums2[pnt2]:
                pnt1 += 1
            elif nums1[pnt1] > nums2[pnt2]:
                pnt2 += 1
            else :
                return nums1[pnt1]
        
        return -1
        

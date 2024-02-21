class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        st1 = set(nums1)
        st2 = set(nums2)
        mat = []
        arr1 = []
        arr2 = []
        for i in st1:
            if i not in st2:
                arr1.append(i)
        
        for j in st2:
            if j not in st1:
                arr2.append(j)
        
        mat.append(arr1)
        mat.append(arr2)
        return mat

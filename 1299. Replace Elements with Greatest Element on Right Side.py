class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        ans.append(-1)
        mx = -1
        for i in range(len(arr)-1,0,-1):
            if arr[i] > mx:
                mx = arr[i]
            
            ans.append(mx)
        
        ans = ans[::-1]
        return ans
        

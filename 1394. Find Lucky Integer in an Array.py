class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mp = Counter(arr)
        mx = -1
        for key,val in mp.items():
            if key == val:
                mx = max(mx,key)
            
        return mx 

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        arr = [0]*n
        for x,y in roads:
            arr[x] += 1
            arr[y] += 1
        
        arr.sort()
        sm = 0
        for i in range(len(arr)):
            sm += (arr[i] *(i+1))
        
        return sm

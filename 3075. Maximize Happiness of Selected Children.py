class Solution:
    def maximumHappinessSum(self, arr: List[int], k: int) -> int:
        arr.sort()
        val = 1
        ind = len(arr) - 2
        
        while ind > -1 and val <= k:
            arr[ind] -= val
            val += 1
            ind -= 1
        
        for i in range(len(arr)):
            if arr[i] < 0:
                arr[i] = 0
        
        return sum(arr[-k:])

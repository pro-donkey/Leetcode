class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        
        mn = 0
        for i in range(1,len(s)):
            mn = abs(int(s[i]) - int(s[i-1]))
            if mn > 2:
                return False
            
        return True 

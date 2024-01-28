class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        cnt = 0
        for i in range(len(s)-1):
            if(s[i] != s[i+1]):
                cnt += 1
        
        
        return cnt

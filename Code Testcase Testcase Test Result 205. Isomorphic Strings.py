class Solution:
    def checkStrs(self, s:str, t:str) -> bool:
        mp = {}
        for i in range(len(s)):
            if s[i] in mp:
                if t[i]!= mp.get(s[i]):
                    return False 
            
            else :
                mp[s[i]] = t[i]

        return True 

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        val1 = self.checkStrs(s,t)
        val2 = self.checkStrs(t,s)

        return val1 and val2


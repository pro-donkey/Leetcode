class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        fst , snd = 0 , 0 
        n, m = len(s),len(t)
        while fst < n and snd < m:
            if s[fst] == t[snd]:
                fst += 1
                snd += 1
            else:
                fst += 1
        
        return m - snd 
        
        

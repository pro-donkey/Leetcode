class Solution:
    def ana(self, a: str, b :str ) -> int:
        ans = 0
        mp = {}
        for ele in b:
            if ele in mp:
                mp[ele] += 1
            else :
                mp[ele] = 1
        cnt = 0
        print(mp)
        for i in a:
            if i in mp and mp[i] > 0:
                
                cnt += 1
                mp[i] -= 1
        print(mp)
        ans = len(b) + len(a) - (2 * cnt)
        return ans
    def minSteps(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        ans = 0
        if m > n:
            ans = self.ana(s, t)
        else :
             ans = self.ana(t,s)

        return ans
        

        

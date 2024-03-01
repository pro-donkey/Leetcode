class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        cnt = 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt += 1
                if cnt != 1:
                    ans += s[i]
            
            elif s[i] == ')':
                cnt -= 1
                if cnt != 0:
                    ans += s[i]
        
        return ans 
        

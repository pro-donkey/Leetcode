class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans,indx = "",-1
        for i in range(len(word)):
            if word[i] == ch:
                indx = i
                break 
        
        ans = word[:indx+1]
        ans = ans[::-1] + word[indx+1:]
        return ans
        

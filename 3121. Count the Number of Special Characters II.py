class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [-1]* 26 
        upper = [len(word) + 1]* 26

        for i in range(len(word)):
            if ord('a') <= ord(word[i]) <= ord('z'):
                lower[ord(word[i]) - ord('a')] = max(lower[ord(word[i]) - ord('a')],i)
            else:
                upper[ord(word[i]) - ord('A')] = min(upper[ord(word[i]) - ord('A')], i)
        


        count = 0
        for i in range(26):
            if  lower[i] != -1 and upper[i] != len(word) + 1 and lower[i] < upper[i]:
                count += 1
        
        return count 
        

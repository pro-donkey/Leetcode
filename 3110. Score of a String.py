class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        if len(s) == 0:
            return score
        for i in range(1, len(s)):
            char1 = ord(s[i]) - ord('a')
            char2 = ord(s[i-1]) - ord('a')
            score += abs(char1 - char2)
        
        return score
        

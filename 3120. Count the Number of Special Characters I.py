class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        hash1 = [0]*26
        hash2 = [0]*26
        for char in word:
            if ord("A") <= ord(char) <= ord("Z"):
                hash1[ord(char) - ord("A")] += 1 
            else:
                hash2[ord(char) - ord("a")] += 1 

        count  = 0
        for i in range(len(hash1)):
            if hash1[i] and hash2[i]:
                count += 1       
        
        return count

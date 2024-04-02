class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for val in magazine:
            if val in mag:
                mag[val] += 1
            else:
                mag[val] = 1
        

        for char in ransomNote:
            if char not in mag:
                return False
            elif mag[char] == 1: del mag[char]
            else:
                mag[char] -= 1
        
        return True

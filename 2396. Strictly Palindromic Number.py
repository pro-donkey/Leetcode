class Solution:
    def to_binary(self, n: int) -> int:
        return bin(n)[2:]
    def isStrictlyPalindromic(self, n: int) -> bool:
        s1 = str(bin(n))
        s2 = s1[::-1]
        if s1 == s2:
            return True
        
        return False

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        val = log10(n)/log10(3)

        return val == int(val)

class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n,'b')
        n = n.zfill(32)

        return int(n[::-1],2)
        

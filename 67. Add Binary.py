class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 ,num2 = int(a,2),int(b,2)
        add = num1 + num2
        return bin(add)[2:]
        

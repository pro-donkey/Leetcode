class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = str(x)
        sm = 0
        for i in s:
            sm += int(i)
        
        if x % sm == 0:
            return sm
        return -1
        

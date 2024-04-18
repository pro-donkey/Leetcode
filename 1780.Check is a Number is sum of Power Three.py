class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            rem = n%3
            if rem == 2:
                return False
            n = n//3 
        
        return True
        

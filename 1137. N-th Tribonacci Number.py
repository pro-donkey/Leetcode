class Solution:
    def tribonacci(self, n: int) -> int:
        fst , scd , thd = 0 , 1, 1
        if n == 0: return 0
        if n < 3:
            return scd
        for i in range(3,n+1):
            res = fst + scd + thd
            fst = scd 
            scd = thd 
            thd = res 
        
        return thd
        

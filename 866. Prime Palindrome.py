class Solution:
    def primeCheck(self, n: int ) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5)+1):
            if n % i == 0:
                return False
        
        return True
    
    def palindrome(self, n : int ) -> bool:
        return str(n) == str(n)[::-1]

    def primePalindrome(self, n: int) -> int:
        while True:
            if self.primeCheck(n) and self.palindrome(n):
                return n
            n += 1
            if 10**7 < n < 10**8:
                n = 10**8

# Solution 1 
class Solution:
    def minOperations(self, n: int) -> int:

        mid = n 
        sm = 0
        for i in range(1,mid,2):
            sm += mid - i 
        

        return sm 

# Solution 2 
class Solution:
    def minOperations(self, n: int) -> int:

        return (n * n) // 4

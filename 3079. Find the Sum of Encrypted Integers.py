class Solution:
    def stringReturn(self, ele : int ) -> str:
        s = str(ele)
        n = len(s)
        if n == 1:
            return s
        mx = 0
        ans = ""
        while ele > 0:
            j = ele%10
            ele = ele//10
            mx = max(mx,j)
        
        ans = str(mx)*n
        return ans
            
            
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        
        
        val = 0
        
        for i in nums:
            val += int(self.stringReturn(i))
            
        
        
        return val
        
        

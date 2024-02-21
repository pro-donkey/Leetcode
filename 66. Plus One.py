class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:
            s += str(i)
        
        val = int(s)
        val += 1
        s = str(val)
        ans = []
        for i in s:
            ans.append(int(i))
        
        return ans
        

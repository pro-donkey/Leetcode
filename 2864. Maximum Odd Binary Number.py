class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        oneCnt = s.count('1')
        return ('1' * (oneCnt - 1)) + ('0'* (len(s) - oneCnt)) + '1'




# Approach 2 
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ans = [*s]
        ans = sorted(ans)
        ans = ans[::-1]
        val = ans.pop(0)
        ans.append(val)
        return "".join(ans)
        

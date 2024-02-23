class Solution:
    def minimumSum(self, num: int) -> int:
        ans = []
        while num:
            rem = num%10
            ans.append(rem)
            num = num // 10
        
        ans = sorted(ans)
        val = 0
        val += ans[1]*10 + ans[2]
        val += ans[0]*10 + ans[3]
        return val

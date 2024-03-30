class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = []
        for ele in nums:
            ans += [str(ele)]
        
        n = len(ans)
        for i in range(n):
            for j in range(i+1,n):
                if (str(ans[i]) + str(ans[j])) > (str(ans[j])+str(ans[i])):
                    continue
                else:
                    ans[i],ans[j] = ans[j],ans[i]
        

        res = ''.join(ans)
        if int(res) == 0:
            return "0"
        return res
        

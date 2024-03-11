class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = ""
        s = str(num)
        cnt = 0
        for i in s:
            if i =='6' and cnt == 0:
                ans += '9'
                cnt += 1
            else :
                ans += i
        return int(ans)
        

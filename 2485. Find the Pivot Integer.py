class Solution:
    def pivotInteger(self, n: int) -> int:
        pre = [0]*n
        suf = [0]*n 
        pre[0] = 1
        suf[n-1] = n
        for i in range(1,n):
            pre[i]  = pre[i-1] + i + 1
        for j in range(n-2,-1,-1):
            suf[j] = suf[j+1] + j + 1
        
        for  i in range(n):
            if pre[i] == suf[i]:
                return i + 1
        
        return -1



class Solution:
    def pivotInteger(self, n: int) -> int:
        x = math.sqrt(n*(n+1)/2)
        num = int(x)
        if num == x:
            return num
        return -1

class Solution:
    
    def func(self,a : int , b : int) -> int:
        val1 = str(a)
        val2 = str(b)
        cnt = 0
        for i in range(0,min(len(val1),len(val2))):
            if val1[i] == val2[i]:
                cnt += 1
            else :
                break
        
        return cnt
        
    
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        mx = -9999
        for i in arr1:
            for j in arr2:
                val = self.func(i,j)
                
                if val > mx:
                    mx = val
        
        
        
        return mx
                



# above is the brute force solution total 699 test cases get passed form this solution 
# below is the solution using trie data structure in python


class Node:
    def __init__(self):
        self.digits = [None] * 10

class Solution:
    def add(self, head, num):
        t = str(num)
        ptr = head
        for c in t:
            if not ptr.digits[int(c)]:
                ptr.digits[int(c)] = Node()
            ptr = ptr.digits[int(c)]

    def check(self, head, num):
        ptr = head
        t = str(num)
        length = 0
        for c in t:
            if ptr.digits[int(c)]:
                length += 1
            else:
                break
            ptr = ptr.digits[int(c)]
        return length

    def longestCommonPrefix(self, arr1, arr2):
        ans = 0
        head = Node()
        for num in arr1:
            self.add(head, num)
        for num in arr2:
            length = self.check(head, num)
            ans = max(ans, length)
        return ans


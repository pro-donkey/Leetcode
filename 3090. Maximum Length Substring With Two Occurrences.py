class Solution:
    def check(self, s: str) -> bool:
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
                if char_count[char] > 2:
                    return False
            else:
                char_count[char] = 1
        return True
    
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 1
        left = 0
        n = len(s)
        right = 1
        while right < n:
            val = s[left:right+1] 
            flag = self.check(val)
            if flag:
                ans = max(ans, right - left + 1)
            else:
                left += 1
            right += 1
        return ans


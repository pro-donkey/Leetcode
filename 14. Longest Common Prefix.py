class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        ans = ""
        left = strs[0]
        right = strs[-1]
        for i in range(min(len(left),len(right))):
            if left[i] != right[i]:
                return ans
            ans += left[i]
        
        return ans

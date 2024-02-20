class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        mx = 0
        sett = set()
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1

            sett.add(s[right])
            mx = max(mx, right - left + 1)

        return mx

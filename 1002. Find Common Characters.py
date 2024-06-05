class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        for char in set(words[0]):
            ans += char * min([word.count(char) for word in words])
        
        return ans
        

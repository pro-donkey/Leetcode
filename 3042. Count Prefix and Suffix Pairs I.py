class Solution:
    
    def func(self, a: str, b: str) -> bool:
        if a == b[:len(a)] and a == b[-len(a):]:
            return True
        return False
    
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if self.func(words[i], words[j]):
                    cnt += 1
        return cnt
        

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        sz = len(s)
        if sz < k:
            return False 
        counter = Counter(s)
        odd_val = 0
        for val,cnt in counter.items():
            if cnt % 2:
                odd_val += 1
        
        if odd_val > k:
            return False 
        
        return True 
        

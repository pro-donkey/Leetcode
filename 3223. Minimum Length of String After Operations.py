class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        sm = 0
        for key,val in counter.items():
            if val <= 2:
                sm += val 
            else:
                if val % 2:
                    sm += 1
                else:
                    sm += 2 
        
        return sm 
        

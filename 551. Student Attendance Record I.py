class Solution:
    def checkRecord(self, s: str) -> bool:
        cnta = 0
        cntl = 0
        for i in s:
            if i == 'A':
                cnta += 1
                cntl = 0
            elif i == 'L':
                cntl += 1
                if cntl == 3:
                    return False
            else:
                cntl = 0

        if cntl < 3 and cnta < 2:
            return True
        return False 
        

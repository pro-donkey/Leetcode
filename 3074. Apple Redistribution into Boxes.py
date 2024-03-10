class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        cnt,cap  = 0,0
        capacity.sort()
        sm = sum(apple)
        for i in range(len(capacity)-1,-1,-1):
            if cap >= sm:
                break
            cap += capacity[i]
            cnt += 1
        
        return cnt

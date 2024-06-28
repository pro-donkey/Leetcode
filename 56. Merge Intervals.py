class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        start, end = intervals[0][0], intervals[0][1]
        ans = []
        for i in range(1, n):
            if end >= intervals[i][0] and end < intervals[i][1]:
                end = intervals[i][1]
            elif end >= intervals[i][1]:
                continue
            else:
                ans.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        ans.append([start, end])
        return ans

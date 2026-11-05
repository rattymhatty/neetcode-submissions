class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        start, count = 0, 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[start][1]:
                count += 1
            else:
                start = i
        return count
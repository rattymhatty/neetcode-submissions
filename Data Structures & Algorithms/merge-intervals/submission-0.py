class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda interval: interval[0])
        merged = [intervals[0]]
        j = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] > merged[j][1]:
                merged.append(intervals[i])
                j += 1
            else:
                merged[j][1] = max(merged[j][1], intervals[i][1])
        return merged
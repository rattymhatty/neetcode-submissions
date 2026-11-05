class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(newInterval) < 2:
            return intervals
        if len(intervals) == 0:
            return [newInterval]
        newInterval = newInterval[:]
        merged = []
        j = -1
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                merged.append(interval)
            elif interval[0] > newInterval[1]:
                j = i
                break
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        merged.append(newInterval)
        if j < 0:
            return merged
        merged.extend(intervals[j:])
        return merged
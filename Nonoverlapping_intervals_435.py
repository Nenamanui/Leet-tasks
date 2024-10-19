class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        point = intervals[0]
        count = 0
        for item in intervals[1:]:
            if item[0] < point[1]:
                count += 1
            else:
                point = item
        return count
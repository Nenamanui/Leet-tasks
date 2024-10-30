class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        output_list = []
        item = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= item[1]:
                item[1] = max(item[1], interval[1])
            else:
                output_list.append(item)
                item = interval
        
        output_list.append(item)

        return output_list
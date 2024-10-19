class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        output_list = []
        intervals.sort(key=lambda x: x[0])
        item = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= item[1]:
                item[1] = max(item[1], interval[1])
            else:
                output_list.append(item)
                item = interval
        
        output_list.append(item)

        return output_list
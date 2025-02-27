import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for point in points:
            distance = point[0] * point[0] + point[1] * point[1]
            item = (-distance, point)
            heapq.heappush(heap, item)
            if len(heap) > k:
                heapq.heappop(heap)
        return [item[1] for item in heap]
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, point in enumerate(points[:k]):
            distance = point[0]*point[0] + point[1]*point[1]
            heapq.heappush(heap, (-distance, i))
        for i, point in enumerate(points[k:]):
            distance = point[0]*point[0] + point[1]*point[1]
            if -distance > heap[0][0]:
                heapq.heapreplace(heap, (-distance, i+k))
        return [points[i] for _, i in heap]
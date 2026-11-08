class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i, num in enumerate(arr[:k]):
            diff = abs(num - x)
            heapq.heappush(heap, (-diff, i))
        for i, num in enumerate(arr[k:]):
            diff = abs(num - x)
            if -diff > heap[0][0]:
                heapq.heapreplace(heap, (-diff, i+k))
        result = [arr[i] for _, i in heap]
        result.sort()
        return result
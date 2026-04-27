class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        res = []
        for p in points:
            x, y = p
            dist = x*x +y*y
            heapq.heappush(max_heap, (-dist, p))
             
            if len(max_heap) > k:
                heapq.heappop(max_heap)
            
        return [p for dist, p in max_heap]
        
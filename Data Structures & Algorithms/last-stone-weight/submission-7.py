class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = []
        for s in stones:
            heapq.heappush(max_heap,-s)

        while len(max_heap)>1:
            s1 = heapq.heappop(max_heap)
            s2 = heapq.heappop(max_heap)

            if s2 > s1:
                heapq.heappush(max_heap, s1 - s2)
        
        return -max_heap[0] if len(max_heap) == 1 else 0


        
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        dq = deque() # pairs of [-cnt, idleTime]
        time = 0
        while max_heap or dq:
            if dq and dq[0][1] == time:
                heapq.heappush(max_heap, dq.popleft()[0])

            if max_heap:
                freq= heapq.heappop(max_heap)+1
                if freq < 0:
                    dq.append((freq, time + n + 1))

            time += 1
        
        return time

        
        



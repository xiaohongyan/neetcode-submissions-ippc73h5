class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        myDict = {}
        max_heap = []

        for s in tasks:
            myDict[s] = myDict.get(s, 0) - 1
        
        # construct max heap: freq, task, tasks in heap are valide to complete
        for key in myDict:
            heapq.heappush(max_heap, (myDict[key], key))

        dq = deque() # pairs of [-cnt, idleTime, task]
        time = 0
        while max_heap or dq:
            if dq :
                freq, remainTime, task = dq[0]
                if remainTime == time:
                    freq, remainTime, task = dq.popleft()
                    heapq.heappush(max_heap, (freq, task))

            if max_heap:
                freq, task = heapq.heappop(max_heap)
                freq += 1
                if freq < 0:
                    dq.append((freq, time + n + 1, task))
                

            time += 1
        
        return time

        
        



class Solution:
    #Dijkstra
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # k 次中转，意味着最多走 k + 1 条边
        # 我们需要存储 0, 1, ..., k+1 种步数的状态
        # 所以空间开 k + 2 即可
        price = [[float('inf')] * (k + 2) for _ in range(n)] # price[city][stopsUsed]
        price[src][0] = 0

        adj = defaultdict(list)

        for f, t, p in flights:
            adj[f].append((t, p))

        minHeap = [(0, src, 0)] #cost, node, stop
        while minHeap:
            cost, n1, stop = heapq.heappop(minHeap)
           
            if n1 == dst: 
                return cost
            
            if stop > k or  price[n1][stop] < cost:
                continue
            
            for n2, w in adj[n1]:
                if price[n2][stop+1] > cost + w:
                    price[n2][stop+1] = cost + w
                    heapq.heappush(minHeap, (price[n2][stop+1], n2, stop + 1))
                
        return  -1

            

            

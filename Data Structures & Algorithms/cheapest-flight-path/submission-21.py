class Solution:
    # Bellman-Ford
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float('inf')] * n
        prices[src] = 0

        dq = deque()
        dq.append((0, src, 0))

        stops = k + 1

        while stops > 0:
            tmpPrices = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if tmpPrices[d] > prices[s] + p: # 不能是tmpPrices[s] 因为tmpPrices[s] 可能已经被更新过, 不在同一层
                   tmpPrices[d] = prices[s] + p
            
            prices = tmpPrices
            stops -= 1

        res = prices[dst]

        return res if res < float('inf') else -1           
    

            
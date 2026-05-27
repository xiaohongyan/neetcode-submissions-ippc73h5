class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
            
        prev = [-prices[0], 0, 0]
        
        def dfs(i):
            nonlocal prev
            if i >= n:
                return

            
            buy = max(prev[0], prev[1] - prices[i])
                
            cooldown = max(prev[1], prev[2])
                
            sell = prev[0] + prices[i]

            prev = [buy, cooldown, sell]
            dfs( i + 1)

        dfs(1)
        return max(prev[1],prev[2])
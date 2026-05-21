class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if not coins:
            return -1
        
        coins.sort(reverse=True)
        n = len(coins)
        INF = float('inf')
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for c in coins:
                if i - c >=0:
                    dp[i] = min(dp[i - c] + 1, dp[i])
        
        return dp[amount] if dp[amount]  != INF else -1

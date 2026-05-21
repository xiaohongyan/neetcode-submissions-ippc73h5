class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if not coins:
            return 0 if amount == 0 else -1
        
        coins.sort()
        n = len(coins)
        INF = float('inf')
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >=0:
                    dp[i] = min(dp[i - c] + 1, dp[i])
                else:
                    # 关键剪枝：因为 coins 是升序的，当前 c 已经太大了，后面的 c 只会更大
                    break
        
        return dp[amount] if dp[amount]  != INF else -1

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
            
        dp = [[0, 0, 0] for _ in range(n)]
        
        dp[0][0] = -prices[0]  # 第 0 天买入
        dp[0][1] = 0           # 第 0 天不持股（未买入）
        dp[0][2] = 0           # 第 0 天不可能有刚卖出的收益
        
        for i in range(1, n):
            # 1. 今天持股：可以是昨天就持股；或者昨天是“可以自由买入的空仓状态”，今天刚买
            # 注意：不能从 dp[i-1][2]（昨天刚卖）转移过来，完美避开冷冻期！
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            
            # 2. 今天是自由空仓：可以是昨天也是自由空仓；或者昨天刚卖了股票（今天冷冻解禁了）
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][2])
            
            # 3. 今天刚卖出：只能是昨天手里有股票，今天卖掉了
            dp[i][2] = dp[i - 1][0] + prices[i]

        # 最后一天的最大利润一定是不持股的状态（自由空仓，或者最后一天刚卖出）
        return max(dp[n - 1][1], dp[n - 1][2])
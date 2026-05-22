class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        capacity = total // 2 

        n = len(stones)

        # dp[j] 表示容量为 j 的背包最多能装多重的石头
        dp = [0] * (capacity + 1)
        dp[0] = 0

        for s in stones:
            for i in range(capacity, s - 1, -1):
                dp[i] = max(dp[i], dp[i - s] + s)

        # dp[target] 是其中一堆石头的最大重量 P
        # 那么另一堆石头的重量 N 就是 total - dp[target]
        # 最终的最小差值就是两者的绝对值差：(total - dp[target]) - dp[target]
        return total - dp[capacity] * 2 
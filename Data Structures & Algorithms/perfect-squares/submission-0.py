class Solution:
    def numSquares(self, n: int) -> int:

        square_root = int(n ** 0.5)
        square = [0] * (square_root + 1)
        for i in range(square_root + 1):
            square[i] = i * i

        dp = [n] * (n + 1)
        # dp[i] the least number of perfect square numbers that sum to i
        dp[0] = 0

        for s in range(1, len(square)):
            cur = square[s]
            for i in range(cur, n + 1):
                dp[i] = min(dp[i], dp[i - cur] + 1)

        return dp[n]
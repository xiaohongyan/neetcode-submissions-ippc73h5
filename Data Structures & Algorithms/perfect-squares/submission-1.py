class Solution:
    def numSquares(self, n: int) -> int:


        # 优化：一行搞定预处理，且只拿 1 开始的有效平方数 [1, 4, 9, 16...]
        # squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        square_root = int(n ** 0.5)
        squares = [0] * (square_root + 1)
        for i in range(square_root + 1):
            squares[i] = i * i


        dp = [n] * (n + 1)
        # dp[i] the least number of perfect squares numbers that sum to i
        dp[0] = 0

        for s in range(1, len(squares)):
            cur = squares[s]
            for i in range(cur, n + 1):
                dp[i] = min(dp[i], dp[i - cur] + 1)

        return dp[n]
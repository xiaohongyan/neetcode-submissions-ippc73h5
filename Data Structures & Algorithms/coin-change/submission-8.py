class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()
        INF = float('inf')

        # dp = -2: not calculated, -1: can't form the amount
        dp = [-2] * (amount + 1)
        dp[0] = 0

        def dfs(remain):

            if remain == 0:
                return 0

            if dp[remain] != -2:
                return dp[remain]

            cur = float('inf')
            for c in coins:
                if remain - c >=0:
                    cnt = dfs(remain -c)
                    if cnt != -1:
                        cur = min(cur, cnt + 1)
                else:
                    break

            dp[remain] = cur if cur != float('inf') else -1

            return dp[remain]

        return dfs(amount)
            

                
        
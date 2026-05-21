class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()
        INF = float('inf')

        # -2: unvisited
        # -1: impossible
        dp = [-2] * (amount + 1)
        dp[0] = 0

        def dfs(remain):

            if remain == 0:
                return 0

            if dp[remain] != -2:
                return dp[remain]

            cur = INF
            for c in coins:
                if c > remain:
                    break

                cnt = dfs(remain -c)
                if cnt != -1:
                    cur = min(cur, cnt + 1)


            dp[remain] = cur if cur != INF else -1

            return dp[remain]

        return dfs(amount)
            

                
        
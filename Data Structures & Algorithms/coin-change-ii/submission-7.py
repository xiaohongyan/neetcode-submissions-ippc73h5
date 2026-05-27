class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        dp = [[-1] * (amount + 1)  for _ in range(n + 1)]
        coins.sort()
        
        def dfs(i, remain):

            if remain == 0 :
                return 1

            if i >= n:
                return 0

            if dp[i][remain] != -1:
                return dp[i][remain]

            if coins[i] > remain:
                return 0
        
            res = dfs(i + 1, remain) + dfs(i, remain - coins[i])
            
            dp[i][remain] = res
            return res

        res = dfs(0, amount)
        return res  if res != -1 else 0
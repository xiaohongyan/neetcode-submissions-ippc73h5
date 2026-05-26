class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1

        coins.sort()
        for c in coins:
            if c > amount:
                break
            for i in range( c, amount + 1):
                dp[i] += dp[i - c]


        return dp[amount]
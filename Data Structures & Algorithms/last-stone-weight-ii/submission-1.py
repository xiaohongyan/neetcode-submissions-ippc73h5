class Solution:
    #
    
    def lastStoneWeightII(self, stones: List[int]) -> int:
       
        total = sum(stones)
        capacity = total // 2 

        n = len(stones)

        # dp[i] max weight for capacity i
        dp = [0] * (capacity + 1)
        dp[0] = 0

        for s in stones:
            for i in range(capacity, s - 1, -1):
                dp[i] = max(dp[i], dp[i - s] + s)


        res = abs(total - dp[capacity] -  dp[capacity])
        return res
        
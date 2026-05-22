class Solution:
    # dp - 1D
    """
    设所有前面放 + 的数字之和为 P。设所有前面放 - 的数字之和为 N。
    我们知道: P + N = sum}(nums)$ 且 P - N = target。
    两式相加: 2P = sum(nums) + target  implies  P = (sum(nums) + target) // 2。
    这不就变成了：从 nums 里挑出一堆数，让他们恰好凑出容量为 P 的背包，问有多少种凑法？
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)
        if (total + target) % 2 != 0:
            return 0
            
        t =  (total + target) // 2

        n = len(nums)

        # dp[i] the number of ways to formed i
        dp = [0] * (t + 1)
        dp[0] = 1
    
        for num in nums:
            for i in range(t, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[t]
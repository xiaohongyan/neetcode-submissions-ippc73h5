class Solution:
    # dp - 1D
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)

        # dp[i] the number of ways each sum can be formed using the first i numbers
        dp = defaultdict(int)
        dp[0] = 1
    
        for i in range(n):
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total - nums[i]] += count
                next_dp[total + nums[i]] += count

            dp =  next_dp
        return dp[target]
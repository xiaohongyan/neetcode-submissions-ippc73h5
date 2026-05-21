class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]  #[max, min]
        res = nums[0]
        dp[0] = [nums[0], nums[0]]

        for i in range(1, n):
            if nums[i] == 0:
                dp[i] = [1, 1]
                res = max(0, res)
            else:
                n1 = dp[i - 1][0] * nums[i]
                n2 = dp[i - 1][1] * nums[i]
                dp[i][0] = max(max(n1, n2), nums[i])
                dp[i][1] = min(min(n1, n2), nums[i])
                res = max(dp[i][0], res)

        return res


        
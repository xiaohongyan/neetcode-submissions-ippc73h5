class Solution:
    # dfs
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}  # (index, total) -> # of ways
        n = len(nums)      

        def dfs(i, curSum):

            if i == n: 
                return 1 if curSum == target else 0

            if (i, curSum) in memo:
                return memo[(i, curSum)]

            memo[(i, curSum)] = dfs(i + 1, curSum - nums[i]) + dfs(i + 1, curSum + nums[i])
            
            return memo[(i, curSum)]


        return dfs(0, 0)


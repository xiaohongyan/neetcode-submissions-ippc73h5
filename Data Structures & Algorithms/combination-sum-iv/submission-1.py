class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        n = len(nums)
        memo = [-1] * (target + 1)

        def dfs(remain):

            if remain == 0:
                return 1

            if memo[remain] != -1:
                return memo[remain]
        
            res = 0
            for num in nums:
                if remain >= num:
                    res += dfs(remain - num)
            
            memo[remain] = res
            return res

        return dfs(target)
            
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = 0
        for num in nums:
            total += num

        if total % 2 != 0:
            return False

        target = total // 2
        nums.sort(reverse=True)
        n = len(nums)

        # memo[i][t] = whether it’s possible to form sum t using elements from index i onward.
        memo = [[-1] * (target + 1) for _ in range(n + 1)] 
        
        def dfs(i, remain):

            if remain == 0:
                return True

            if i >= n or remain < 0:
                return False

            if memo[i][remain] != -1:
                return memo[i][remain]

            if  remain - nums[i] >= 0 and dfs(i + 1, remain - nums[i]): 
                memo[i][remain] = True 
                return True
           
            memo[i][remain] = dfs(i + 1, remain)
            return memo[i][remain]

        return dfs(0, target)


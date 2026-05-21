class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        n = len(nums)
        memo = [-1] * n
        res = 0
  
        def dfs(i):  # the length of the longest increasing subsequence starting at index i
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]

            cur = 1
            for j in range(i + 1, n):
                tmp = 1
                if nums[j] > nums[i]:
                    tmp += dfs(j)
                    cur = max(cur, tmp)

            memo[i] = cur
            return cur

        return max(dfs(i) for i in range(n))


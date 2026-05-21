class Solution:
    def maxProduct(self, nums: List[int]) -> int:
       
        if not nums:
            return 0
        
        n = len(nums)
        res = nums[0]

        prefix, suffix = 0, 0
        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)

            res = max(res, max(prefix, suffix))

        return res
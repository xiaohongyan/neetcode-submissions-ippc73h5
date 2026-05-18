class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        n = len(nums)
        res = nums[0]

        for i in range(n - 1):
            tmp = rob2
            rob2 = max(rob2, rob1 + nums[i])
            rob1 = tmp
        res = max(rob2, res)

        rob1 = 0
        rob2 = 0
        for i in range(1, n):
            tmp = rob2
            rob2 = max(rob2, rob1 + nums[i])
            rob1 = tmp

        res = max(rob2, res)
        return res

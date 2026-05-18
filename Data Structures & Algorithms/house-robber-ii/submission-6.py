class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if not nums:
            return 0
        
        if n == 1:
            return nums[0]

        def helper(houses):
            rob1, rob2 = 0, 0

            for num in houses:
                tmp = rob2
                rob2 = max(rob2, rob1 + num)
                rob1 = tmp
            return rob2

        return max(helper(nums[1:]), helper(nums[:-1]))

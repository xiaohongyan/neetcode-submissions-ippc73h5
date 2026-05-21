class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        n = len(nums)

        res = nums[0]
        curMax, curMin = 1, 1

        for num in nums:
            n1 = curMax * num
            n2 = curMin * num
            curMax = max(max(n1, n2), num)
            curMin = min(min(n1, n2), num)
            res = max(curMax, res)

        return res


        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2 
        sumSet = set()
        sumSet.add(0)

        for num in nums:
            tmp = sumSet.copy()
            for e in tmp:
                cur = e + num
                if cur == target:
                    return True
                if cur > target:
                    continue
                sumSet.add(cur)

        return False
        
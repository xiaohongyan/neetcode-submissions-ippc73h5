class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (r - l) //2 + l

            if nums[m] == target:
                return True

            if nums[l] < nums[m]: # m is on the left portion
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else: 
                    l = m + 1
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r  = m -1 
            else:
                l += 1

        return False

            
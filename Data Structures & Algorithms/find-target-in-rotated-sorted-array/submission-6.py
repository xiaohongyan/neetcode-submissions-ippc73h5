class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l, r = 0, n-1
        while l<=r:
            m = (r - l) //2 + l

            if nums[m] == target:
                return m

            elif nums[l] <= nums[m]: # m is on the left portion
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else: 
                    l = m + 1
            else:  
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r  = m -1
        
        return -1

         
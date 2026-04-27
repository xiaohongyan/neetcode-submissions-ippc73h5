import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        def partition(nums, left, right):
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            pivot = nums[right]

            i = left
            for j in range(left, right):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                
            nums[i], nums[right] = nums[right], nums[i]
            
            return i

        target_idx = len(nums) - k
        left = 0
        right =len(nums) - 1
        while True:
            idx = partition(nums, left, right)
            if idx == target_idx:
                return nums[target_idx]
            if idx < target_idx:
                left = idx + 1
            else:
                right = idx - 1

        return nums[target_idx]
                
            


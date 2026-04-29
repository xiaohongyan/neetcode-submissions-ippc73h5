
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        count = {n: 0 for n in nums}
        for num in nums:
            count[num] += 1

        def backtracking():

            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for num in count:
                if count[num]> 0:
                    cur.append(num)
                    count[num] -= 1

                    backtracking()

                    cur.pop()
                    count[num] += 1
            
        backtracking()
        return res
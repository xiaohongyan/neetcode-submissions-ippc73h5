class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            for i in range(len(res)):
                # res[i] + [n] 会创建一个新的列表对象
                res.append(res[i] + [n])

        return res
        
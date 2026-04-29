class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)
        res = []
        cur = []

        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                cur.append(nums[i])
                visited[i] = True
                dfs()

                cur.pop()
                visited[i] = False
            
        dfs()
        return res


        
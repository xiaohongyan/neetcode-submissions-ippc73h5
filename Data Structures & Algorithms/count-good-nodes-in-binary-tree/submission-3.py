# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        cnt = 0
        cur_max = -float('inf')

        def dfs(node, cur_max):
            nonlocal cnt

            if not node:
                return

            if node.val >= cur_max:
                cnt += 1
                cur_max = node.val
            
            dfs(node.left, cur_max)
            dfs(node.right, cur_max)
            return

        dfs(root, cur_max)

        return cnt

        



        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        cur_max = -float('inf')

        def dfs(node, cur_max):

            if not node:
                return 0

            is_good = 1 if node.val >= cur_max else 0
            cur_max = max(node.val, cur_max)
            
            return  is_good + dfs(node.left, cur_max) + dfs(node.right, cur_max)

        return  dfs(root, cur_max)

        



        
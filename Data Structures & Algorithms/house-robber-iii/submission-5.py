# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return [0, 0]  #[rob_val, skip_val]

            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            # rob current node
            rob_val = node.val + left_skip + right_skip

            # skip current node
            skip_val = max(left_rob, left_skip)  + max(right_rob, right_skip) 

            return [rob_val, skip_val]

        res = dfs(root)
        return max(res[1], res[0])
        
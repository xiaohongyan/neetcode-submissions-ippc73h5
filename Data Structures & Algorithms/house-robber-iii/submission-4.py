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

            left =  dfs(node.left)
            right =  dfs(node.right)

            # rob current node
            rob_val = node.val + left[1] + right[1]

            # skip current node
            skip_val = max(left[1], left[0])  + max(right[0], right[1]) 

            return [rob_val, skip_val]
            
        res = dfs(root)
        return max(res[1], res[0])
        
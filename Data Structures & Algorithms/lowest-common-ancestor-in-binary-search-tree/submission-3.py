# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root or not p or not q:
            return None

        p_val, q_val = min(p.val, q.val), max(p.val, q.val) 
        
        def dfs(cur):

            if not cur:
                return None

            if p_val <= cur.val <= q_val:
                return cur

            if cur.val > q_val:
                return dfs(cur.left)
            else:
                return dfs(cur.right)
            
        return dfs(root)
            
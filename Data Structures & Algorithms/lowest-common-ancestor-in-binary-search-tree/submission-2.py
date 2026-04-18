# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val > q.val: # make sure q.val > p.val
            tmp = p
            p = q
            q = tmp
        
        def dfs(cur):

            if not cur:
                return None

            if p.val <= cur.val <= q.val:
                return cur

            if cur.val > q.val:
                return dfs(cur.left)
            else: #cur.val < p.val
                return dfs(cur.right)
            
        return dfs(root)
            
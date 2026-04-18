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

        stack = [root]
        p_val, q_val = min(p.val, q.val), max(p.val, q.val) 
        while stack:
            cur = stack.pop()

            if p_val <= cur.val <= q_val:
                return cur

            if cur.val > q_val:
                stack.append(cur.left)
            else:
                stack.append(cur.right)

        return None
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        dq = deque([(root, 0)])
        res = 0
        while dq:
            cur, val = dq.popleft()

            val = val * 10 + cur.val
            if not cur.left and not cur.right:
                res += val
                continue

            if cur.left:
                dq.append((cur.left, val))
            if cur.right:
                dq.append((cur.right, val))
        return res


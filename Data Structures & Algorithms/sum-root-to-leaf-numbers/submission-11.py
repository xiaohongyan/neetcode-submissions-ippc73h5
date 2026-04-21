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
            cur, num = dq.popleft()

            num = num * 10 + cur.val
            if not cur.left and not cur.right:
                res += num
                continue

            if cur.left:
                dq.append((cur.left, num))
            if cur.right:
                dq.append((cur.right, num))
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        dq = deque([(root, targetSum- root.val)])

        while dq:
            for _ in range(len(dq)):
                cur, cur_target = dq.popleft()
                if not cur.left and not cur.right and cur_target == 0:
                    return True
                if cur.left:
                    dq.append((cur.left, cur_target-cur.left.val))
                if cur.right:
                    dq.append((cur.right, cur_target-cur.right.val))

        return False
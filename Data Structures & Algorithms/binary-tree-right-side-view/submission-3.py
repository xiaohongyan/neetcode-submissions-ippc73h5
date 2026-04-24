# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        dq = deque([root])

        while dq:
            for _ in range(len(dq)):
                cur = dq.popleft()
                val = cur.val  # val will be the last value pop from the queue
                
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)

            res.append(val)
            
        return res

        
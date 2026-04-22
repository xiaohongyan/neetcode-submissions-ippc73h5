# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root: 
            return 0

        dq = deque([(root,  -float('inf'))])
        cnt = 0

        while dq:
            for _ in range(len(dq)):
                cur, cur_max = dq.popleft()

                if cur.val >= cur_max:
                    cur_max = cur.val
                    cnt += 1

                if cur.left:
                    dq.append((cur.left, cur_max))
                if cur.right:
                    dq.append((cur.right, cur_max))

        return cnt
        
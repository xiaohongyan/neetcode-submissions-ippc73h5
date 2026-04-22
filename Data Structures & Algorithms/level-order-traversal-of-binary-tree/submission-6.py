# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       
        res = []
        if not root:
            return res

        dq = deque([root])

        while dq:
            lst = []
            for _ in range(len(dq)):
                cur = dq.popleft()
                lst.append(cur.val)

                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            
            res.append(lst)
        
        return res
                


        
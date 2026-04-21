# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0

        stack = [(root, 0)]
        res = 0
        num = 0
        while stack:
            cur, num = stack.pop()
            num = num * 10 + cur.val
            
            if not cur.left and not cur.right:
                res += num
                continue
            
            if cur.left:
                stack.append((cur.left, num))
            if cur.right:
                stack.append((cur.right, num))
        
        return res




        
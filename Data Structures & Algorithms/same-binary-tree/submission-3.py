# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        stack = [(p, q)]
        while stack:
            cur1, cur2 = stack.pop()

            if not cur1 and not cur2:
                continue
            if not cur1 or not cur2 or cur1.val != cur2.val:
                return False
            
            stack.append((cur1.left, cur2.left))
            stack.append((cur1.right, cur2.right))
        
        return True
            
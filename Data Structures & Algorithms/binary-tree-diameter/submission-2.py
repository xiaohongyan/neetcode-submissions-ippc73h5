# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        stack = [root]
        mp = {None: (0, 0)} # max height, diameter, base case
        cur = root

        while stack:
            cur = stack[-1]
            if cur.left and cur.left not in mp:
                stack.append(cur.left)
            elif cur.right and cur.right not in mp:
                stack.append(cur.right)
            else:
                cur = stack.pop()
                leftHeight, leftDiameter = mp[cur.left]
                rightHeight, rightDiameter = mp[cur.right]

                mp[cur] = (1 + max(leftHeight, rightHeight), max(leftHeight + rightHeight, leftDiameter, rightDiameter))
        return mp[root][1]
            

                
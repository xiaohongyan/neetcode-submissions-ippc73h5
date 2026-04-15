# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        lst1 =[]
        lst2 =[]

        def serialzie(node):
            if not node:
                return '#'
            
            return f"({node.val})" + serialzie(node.left) + serialzie(node.right)

        root_str = serialzie(root)
        sub_str = serialzie(subRoot)

        return sub_str in root_str
        

        
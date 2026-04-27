# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashMap = {}

        for i in range(len(inorder)):
            hashMap[inorder[i]] = i
        
        cur_idx = 0
        def dfs(start, end):
            nonlocal cur_idx

            if start > end:
                return None

            cur_val = preorder[cur_idx]
            node = TreeNode(cur_val)
            mid_idx = hashMap[cur_val]
            cur_idx += 1
            
            node.left = dfs(start,  mid_idx -1 )
            node.right = dfs( mid_idx + 1, end)
            return node
        
        return dfs(0, len(inorder) -1)





        

        
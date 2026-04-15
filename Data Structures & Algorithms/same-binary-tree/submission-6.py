# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        dq1 = deque([p])
        dq2 = deque([q])

        while dq1 and dq2:

            for _ in range(len(dq1)):
                cur1= dq1.popleft()
                cur2= dq2.popleft()

                if not cur1 and not cur2:
                    continue

                if not cur1 and cur2 or cur1 and not cur2 or cur1.val != cur2.val:
                    return False
            

                dq1.append(cur1.left)
                dq2.append(cur2.left)
                dq1.append(cur1.right)
                dq2.append(cur2.right)

        return True
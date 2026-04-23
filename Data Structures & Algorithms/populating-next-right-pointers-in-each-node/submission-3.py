"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root: return root
        
        dq = deque([root])

        while dq:
            nxt = None
            for _ in range(len(dq)):
                cur = dq.popleft()
                cur.next = nxt
                nxt = cur

                if cur.right:
                    dq.append(cur.right)
                if cur.left:
                    dq.append(cur.left)

        return root

                


        
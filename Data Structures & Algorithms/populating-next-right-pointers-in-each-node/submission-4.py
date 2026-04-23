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

        start = root
        while start:
            cur = start
            start  = start.left
            prev = None
            while cur:
                if cur.left and cur.right:
                    cur.left.next = cur.right
                    cur.right.next = None

                    if prev:
                        prev.next = cur.left
                
                prev = cur.right
                cur = cur.next
                
        return root


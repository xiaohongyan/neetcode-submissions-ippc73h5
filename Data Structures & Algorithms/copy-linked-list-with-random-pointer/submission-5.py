"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        curr = head   
        nodeList = {None: None}  # none map to none {old_node: new_node}
        
        def getClone(curr)->Node:
            if curr not in nodeList:
                nodeList[curr] =  Node(curr.val)
            return nodeList[curr]

        while curr:
            clone = getClone(curr)
            clone.next = getClone(curr.next)
            clone.random = getClone(curr.random)
            curr = curr.next
        return nodeList[head]
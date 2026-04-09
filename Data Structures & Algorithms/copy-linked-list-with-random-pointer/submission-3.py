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
        #nodeList = {-1: None}  # {index: new_node}
        copy = Node(0)
        
        index = 0

        while curr:

            if curr in nodeList:
                copy.next = nodeList[curr]
            else:
                new_node = Node(curr.val)
                copy.next = new_node
                nodeList[curr] = new_node
            
            copy = copy.next

            if curr.random in nodeList:
                copy.random = nodeList[curr.random]
            else:
                new_node = Node(curr.random.val)
                copy.random = new_node
                nodeList[curr.random] = new_node

            curr = curr.next
        return nodeList[head]
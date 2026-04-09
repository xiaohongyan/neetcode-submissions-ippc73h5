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
        while curr:
            new_node = Node(curr.val)
            nodeList[curr] = new_node
            curr = curr.next
       
        curr = head
        while curr:
            copy = nodeList[curr]
            copy.random = nodeList[curr.random]
            copy.next = nodeList[curr.next]
            curr = curr.next

        return nodeList[head]


        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       
        if not head:
            return head

        curr = tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1

        k = k % n

        if k == 0:
            return head

        for _ in range (n - k - 1):  # find the node to break
            curr = curr.next
  
        new_head = curr.next
        curr.next = None
        tail.next = head

        return new_head
        


        

        
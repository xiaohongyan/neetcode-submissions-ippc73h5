# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       
        if not head:
            return head

        curr = head
        n = 1
        while curr.next:
            curr = curr.next  # curr is the tail
            n +=1

        k = k % n

        if k == 0:
            return head

        curr.next = head

        for _ in range (n - k):  # find the node to break
            curr = curr.next
  
        new_head = curr.next
        curr.next = None
        return new_head
        


        

        
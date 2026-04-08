# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        i = n+1  # fast is one step further so slow.next is the one to be removed
        while i > 0:
            fast = fast.next
            i -= 1
        
        while fast:
            fast = fast.next
            slow = slow.next # slow.next is the one to be removed
        
        slow.next = slow.next.next
        
        return dummy.next

        
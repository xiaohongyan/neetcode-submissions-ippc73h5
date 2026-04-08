# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # reverse the second half
        second  = slow.next  #second is shorter or equal to first 
        prev = slow.next = None
        while second :
            next_tmp = second .next
            second .next = prev
            prev = second 
            second  = next_tmp
        
        first = head
        second = prev
        while second:  # l2 is shorter or equal to l1
            next_tmp_1 = first.next
            next_tmp_2 = second.next
            first.next = second
            second.next = next_tmp_1
            first = next_tmp_1
            second = next_tmp_2
        




        
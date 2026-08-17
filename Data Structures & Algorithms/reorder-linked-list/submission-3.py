# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        slow_ptr = head
        fast_ptr = head.next

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        second_part = slow_ptr.next
        slow_ptr.next = None

        reversed_part = None
        tmp = None
        while second_part:
            tmp = second_part.next
            second_part.next = reversed_part
            reversed_part = second_part
            second_part = tmp
        
        reversed_tmp = None
        first_part_tmp = None
        dummy = head
        while reversed_part and dummy:
            first_part_tmp = dummy.next
            reversed_tmp = reversed_part.next
            reversed_part.next = first_part_tmp
            dummy.next = reversed_part
            reversed_part = reversed_tmp
            dummy = dummy.next.next
        
        if reversed_part:
            dummy.next = reversed_part




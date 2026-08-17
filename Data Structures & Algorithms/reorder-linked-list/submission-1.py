# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        mid_pointer = head
        faster_pointer = head.next          # FIX: start one ahead so first half is longer

        while faster_pointer and faster_pointer.next:
            mid_pointer = mid_pointer.next
            faster_pointer = faster_pointer.next.next   # FIX: two steps, not one

        reversed_half = None
        tmp = None

        second = mid_pointer.next           # FIX: split the list
        mid_pointer.next = None             # FIX: otherwise you build a cycle
        mid_pointer = second

        while mid_pointer:
            tmp = mid_pointer.next
            mid_pointer.next = reversed_half
            reversed_half = mid_pointer
            mid_pointer = tmp

        dummy = res = ListNode()
        while reversed_half and head:
            next_head = head.next                   # FIX: save both successors
            next_rev = reversed_half.next           #      BEFORE rewiring
            dummy.next = head
            head.next = reversed_half
            dummy = reversed_half
            head = next_head
            reversed_half = next_rev

        if reversed_half:
            dummy.next = reversed_half
        if head:
            dummy.next = head               # FIX: was dummy.next = dummy (self-loop)
        # FIX: removed `head = res.next` — rebinding a local does nothing,
        #      and the list is already reordered in place
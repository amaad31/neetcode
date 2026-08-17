# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        nxt = head
        nxt_to_nxt = head

        while nxt_to_nxt and nxt_to_nxt.next:
            nxt = nxt.next
            nxt_to_nxt = nxt_to_nxt.next.next
            if nxt == nxt_to_nxt:
                return True
        return False


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr_node = head
        faster_curr_node = head
        while faster_curr_node and faster_curr_node.next:
            curr_node = curr_node.next
            faster_curr_node = faster_curr_node.next.next
            if curr_node == faster_curr_node:
                return True
        return False
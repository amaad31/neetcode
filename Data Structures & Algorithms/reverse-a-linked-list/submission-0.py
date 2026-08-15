# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        res_head = None
        cur_node = head
        while cur_node:
            next_node = cur_node.next
            temp_res_next = res_head
            res_head = cur_node
            res_head.next = temp_res_next
            cur_node = next_node
        return res_head
        
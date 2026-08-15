# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng = 0
        temp_head = head
        while temp_head:
            leng += 1
            temp_head = temp_head.next
        idx_remove = leng - n + 1
        cur_idx = 1
        dummy = ListNode()
        res = dummy
        while head:
            if cur_idx != idx_remove:
                res.next = head
                res = res.next
            head = head.next
            cur_idx += 1
        
        res.next = None
        return dummy.next
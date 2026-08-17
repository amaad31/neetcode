# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        if n <= 0:
            return head

        count = 0
        tmp_head = head

        while tmp_head:
            count += 1
            tmp_head = tmp_head.next
        
        new_n = count - n
        if new_n == 0:
            return head.next

        count = 1
        dummy = head
        
        while dummy:
            if count == new_n:
                dummy.next = dummy.next.next
                break 
            count += 1
            dummy = dummy.next
        return head
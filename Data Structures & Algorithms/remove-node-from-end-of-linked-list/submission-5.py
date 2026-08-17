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
                if dummy.next.next:
                    to_be_del = dummy.next
                    to_be_del = None
                    del to_be_del
                    tmp_head = dummy.next.next
                    dummy.next = tmp_head
                else:
                    dummy.next = None
                break 
            count += 1
            dummy = dummy.next
        
        return head
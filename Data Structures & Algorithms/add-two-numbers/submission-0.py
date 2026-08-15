# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1, curr_l2 = l1, l2
        dummy = ListNode()
        res = dummy
        carry_forward = 0
        while(curr_l1 or curr_l2 or carry_forward):
            curr_l1_val = 0 if not curr_l1 else curr_l1.val
            curr_l2_val = 0 if not curr_l2 else curr_l2.val
            local_sum = curr_l1_val + curr_l2_val + carry_forward
            res.next = ListNode(local_sum % 10)
            carry_forward = local_sum // 10
            curr_l1 = None if not curr_l1 else curr_l1.next
            curr_l2 = None if not curr_l2 else curr_l2.next
            res = res.next

        return dummy.next





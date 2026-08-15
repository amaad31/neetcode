# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif (not p and q) or (p and not q):
            return False
        stack_p = [p]
        stack_q = [q]
        while stack_p and stack_q:
            curr_p = stack_p.pop()
            curr_q = stack_q.pop()
            if curr_p.val != curr_q.val:
                return False
            if curr_p.right and curr_q.right:
                stack_q.append(curr_q.right)
                stack_p.append(curr_p.right)
            elif (curr_p.right and not curr_q.right) or (not curr_p.right and curr_q.right):
                return False
            if curr_p.left and curr_q.left:
                stack_q.append(curr_q.left)
                stack_p.append(curr_p.left)
            elif (curr_p.left and not curr_q.left) or (not curr_p.left and curr_q.left):
                return False
        return True
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = [root]
        while stack:
            cur_node = stack.pop()
            if (p.val <= cur_node.val and cur_node.val <= q.val) or (q.val <= cur_node.val and cur_node.val <= p.val):
                return cur_node
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
        return None

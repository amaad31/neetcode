# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        res = root
        root_stack = [root]
        while root_stack:
            curr_node = root_stack.pop()
            res = curr_node
            #if curr_node.val == p.val or curr_node.val == q.val or not (curr_node.val < p.val and curr_node.val < q.val) or not (curr_node.val > p.val and curr_node.val > q.val):
            #    break
            if curr_node.val < p.val and curr_node.val < q.val:
                root_stack.append(curr_node.right)
            elif curr_node.val > p.val and curr_node.val > q.val:
                root_stack.append(curr_node.left)
            else:
                break
        return res




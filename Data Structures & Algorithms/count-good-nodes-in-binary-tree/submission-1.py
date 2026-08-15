# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.res = 0
        def findGoodNodes(node, max_branch_val):
            if not node:
                return
            if node.val >= max_branch_val:
                self.res += 1
                max_branch_val = node.val
            left_node = findGoodNodes(node.left, max_branch_val)
            right_node = findGoodNodes(node.right, max_branch_val)
        findGoodNodes(root, root.val)
        return self.res
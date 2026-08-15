# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            True
        def dfs(node):
            if not node:
                return 0, True
            left_depth, res_left = dfs(node.left)
            right_depth, res_right = dfs(node.right)
            local_res = True if abs(right_depth - left_depth) < 2 else False
            return (1 + max(left_depth, right_depth), (local_res and res_left and res_right))
        depth, res = dfs(root)
        return res

        
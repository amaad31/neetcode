# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(cur_node):
            if not cur_node:
                return 0
            
            return max(dfs(cur_node.left) + 1, dfs(cur_node.right) + 1)
        
        return dfs(root)
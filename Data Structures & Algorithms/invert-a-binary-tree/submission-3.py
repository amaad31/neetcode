# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        def dfs(cur_root):
            cur_root.left, cur_root.right = cur_root.right, cur_root.left
            if cur_root.left:
                dfs(cur_root.left)
            if cur_root.right:
                dfs(cur_root.right)
            
        dfs(root)
        
        return root
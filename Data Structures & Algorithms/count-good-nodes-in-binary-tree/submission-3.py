# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res = 0
        def dfs(node, cur_max):
            if not node:
                return
            nonlocal res
            if node.val >= cur_max:
                cur_max = node.val
                res += 1
            
            dfs(node.left, cur_max)
            dfs(node.right, cur_max)

        
        dfs(root, float('-inf'))
        return res
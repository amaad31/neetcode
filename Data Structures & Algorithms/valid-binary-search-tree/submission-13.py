# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur_node, cur_min, cur_max):
            if not cur_node:
                return True
            
            if not (cur_min < cur_node.val and cur_node.val < cur_max):
                return False
            return dfs(cur_node.left, min(cur_min, cur_node.val), min(cur_max, cur_node.val)) and dfs(cur_node.right, max(cur_min, cur_node.val), max(cur_max, cur_node.val))
        
        return dfs(root, float('-inf'), float('inf'))

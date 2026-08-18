# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        res_arr = []
        def dfs(cur_node):
            if not cur_node:
                return
            
            dfs(cur_node.left)
            res_arr.append(cur_node.val)
            dfs(cur_node.right)
        dfs(root)
        return res_arr[k - 1]

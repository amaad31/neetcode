# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        sol_map = defaultdict(int)
        
        def dfs(node, lvl):
            if not node:
                return
            
            sol_map[lvl] = node.val
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)
        
        dfs(root, 1)
        return list(sol_map.values())
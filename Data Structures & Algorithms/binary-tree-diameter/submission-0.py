# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.idx = 1
        self.res = 0
    
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            print(f"{self.idx}) {left} & {right}, node: {node.val}")
            self.idx = self.idx + 1
            self.res = max(self.res, (left + right))
            return 1 + max(right, left)
        dfs(root)
        return self.res
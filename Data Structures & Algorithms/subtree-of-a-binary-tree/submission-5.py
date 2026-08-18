# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        def isSame(p, q):
            if not p and not q:
                return True
            elif ((p and not q) or (q and not p)) or (p.val != q.val):
                return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        
        stack = [root]
        last_same_node = None
        while stack:
            cur_node = stack.pop()
            if isSame(cur_node, subRoot):
                return True
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)

        return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_stack = [root]
        while root_stack:
            curr_node = root_stack.pop()
            if curr_node.val == subRoot.val:
                subRoot_stack = [subRoot]
                root_subStack = [curr_node]
                subtree_found = True
                while root_subStack or subRoot_stack:
                    if (root_subStack and not subRoot_stack) or (not root_subStack and subRoot_stack):
                        subtree_found = False
                        break
                    curr_subroot_node = subRoot_stack.pop()
                    curr_root_node = root_subStack.pop()
                    if curr_subroot_node.val != curr_root_node.val:
                        subtree_found = False
                        break
                    if curr_subroot_node.left:
                        subRoot_stack.append(curr_subroot_node.left)
                    if curr_root_node.left:
                        root_subStack.append(curr_root_node.left)
                    if curr_subroot_node.right:
                        subRoot_stack.append(curr_subroot_node.right)
                    if curr_root_node.right:
                        root_subStack.append(curr_root_node.right)
                if subtree_found:
                    return True
            if curr_node.left:
                root_stack.append(curr_node.left)
            if curr_node.right:
                root_stack.append(curr_node.right)
        return False
                    
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
        node_stack = [root]
        while(node_stack):
            curr_node = node_stack.pop()
            left_node = curr_node.left
            right_node = curr_node.right
            if left_node:
                node_stack.append(left_node)
            if right_node:
                node_stack.append(right_node)
            temp_node = left_node
            curr_node.left = right_node
            curr_node.right = temp_node
        return root
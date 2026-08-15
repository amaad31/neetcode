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
        level_hashmap = defaultdict(list)
        node_stack = [(root, 1)]
        while node_stack:
            curr_node, curr_level = node_stack.pop()
            level_hashmap[curr_level].append(curr_node.val)
            if curr_node.left:
                node_stack.append((curr_node.left, (curr_level + 1)))
            if curr_node.right:
                node_stack.append((curr_node.right, (curr_level + 1)))
        res = []
        for _, values in level_hashmap.items():
            res.append(values[0])
        return res

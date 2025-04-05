# Last updated: 4/5/2025, 3:59:34 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return 
        stack = [root]
        prev_node = TreeNode()
        while stack:
            node = stack.pop(-1)
            prev_node.right = node
            prev_node.left = None
        
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            prev_node = node
# Last updated: 5/8/2025, 11:40:39 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, curr_depth):

        if node.left is None and node.right is None:
            self.max_depth = max(self.max_depth, curr_depth)
            return

        if node.left:
            self.traverse(node.left, curr_depth+1)
        
        if node.right:
            self.traverse(node.right,curr_depth+1)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        self.max_depth = 0

        self.traverse(root, 1)
        return self.max_depth
        
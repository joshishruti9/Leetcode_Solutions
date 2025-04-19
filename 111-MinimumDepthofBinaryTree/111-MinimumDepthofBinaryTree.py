# Last updated: 4/19/2025, 1:56:46 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, node, curr_length):

        if node.left is None and node.right is None:
            self.min_length = min(self.min_length, curr_length)
            return

        if node.left:
            self.traverse(node.left, curr_length + 1)
        if node.right:
            self.traverse(node.right, curr_length + 1)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.min_length = float("inf")
        self.traverse(root, 1)
        
        return self.min_length
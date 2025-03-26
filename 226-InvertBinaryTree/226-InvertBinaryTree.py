# Last updated: 3/26/2025, 4:12:59 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):

        temp = node.left
        node.left = node.right
        node.right = temp

        if node.left:
            self.traverse(node.left)
        if node.right:
            self.traverse(node.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        self.traverse(root)
        return root
        
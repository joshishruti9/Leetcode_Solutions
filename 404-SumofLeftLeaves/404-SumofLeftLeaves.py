# Last updated: 4/13/2025, 3:37:59 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, flag):
        
        if node.left is None and node.right is None and flag is True:
            self.total += node.val
            return

        if node.left:
            self.traverse(node.left,True)
        if node.right:
            self.traverse(node.right,False)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.total = 0
        self.traverse(root, False)

        return self.total
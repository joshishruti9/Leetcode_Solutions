# Last updated: 4/13/2025, 3:39:54 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, flag, total):
        
        if node.left is None and node.right is None and flag is True:
            total += node.val
            return total

        ltotal = rtotal = 0

        if node.left:
            ltotal = self.traverse(node.left,True, total)
        if node.right:
            rtotal = self.traverse(node.right,False, total)

        return ltotal + rtotal

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        total = 0
        total = self.traverse(root, False, total)

        return total
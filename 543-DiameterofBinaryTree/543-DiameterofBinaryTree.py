# Last updated: 5/9/2025, 11:28:33 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        if node.left is None and node.right is None:
            return 1
        
        l_depth = r_depth = 0
        if node.left:
            l_depth = self.traverse(node.left)
        if node.right:
            r_depth = self.traverse(node.right)

        self.max = max(self.max, (l_depth+r_depth))

        return max(l_depth,r_depth)+1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        self.max = 0
        self.traverse(root)

        return self.max
        
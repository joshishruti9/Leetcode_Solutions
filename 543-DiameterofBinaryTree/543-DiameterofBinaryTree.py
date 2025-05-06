# Last updated: 5/5/2025, 10:27:02 PM
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

        l_len = r_len = 0

        if node.left:
            l_len = self.traverse(node.left)
        if node.right:
            r_len = self.traverse(node.right)

        self.max = max(self.max, (l_len + r_len))
        
        return max(r_len, l_len) + 1
       

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.max = 0
        max_len = self.traverse(root)

        return self.max
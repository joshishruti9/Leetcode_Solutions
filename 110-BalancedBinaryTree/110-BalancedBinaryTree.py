# Last updated: 5/8/2025, 11:52:45 PM
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

        l_height = r_height = 0
        if node.left:
            l_height = self.traverse(node.left)
        
        if node.right:
            r_height = self.traverse(node.right)
        
        if abs(l_height - r_height) > 1:
            self.flag = False
        
        return max(l_height, r_height) + 1
        


    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        self.flag = True
        self.traverse(root)
        return self.flag

        
        
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
        
        lcount = rcount = 0

        if node.left:
            lcount = self.traverse(node.left)
        
        if node.right:
            rcount = self.traverse(node.right)
        
        return lcount + rcount + 1

    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        return self.traverse(root)
        

        
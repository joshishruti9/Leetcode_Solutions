# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        if node is None:
            return None, None
        
        if node.left is None and node.right is None:
            return node, node

        lstart , lend = self.traverse(node.left)
        rstart , rend = self.traverse(node.right)
        
        if lstart:
            node.right = lstart
            lend.right = rstart
            node.left = None
        
        return node, rend if rend != None else lend 


    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if root:
            self.traverse(root)

        
        
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
       
        lnode, llast_node = self.traverse(node.left)
        rnode, rlast_node = self.traverse(node.right)
        
        if node.left:
            node.left = None
            llast_node.right = rnode
            node.right = lnode
            
        return node, rlast_node or llast_node or node



    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        self.traverse(root)
        

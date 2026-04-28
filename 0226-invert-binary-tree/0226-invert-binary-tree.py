# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        if node.left is None and node.right is None:
            return
        
        temp = node.left
        node.left = node.right
        node.right = temp
        
        if node.left:
            self.traverse(node.left)
        
        if node.right:
            self.traverse(node.right)
        
        return

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
            
        self.traverse(root)
        return root
        
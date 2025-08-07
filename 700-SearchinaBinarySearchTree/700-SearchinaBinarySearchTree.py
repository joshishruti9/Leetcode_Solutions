# Last updated: 8/7/2025, 3:33:05 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, val):
       
        if val == node.val:
            return node
        
        if node.left is None and node.right is None:
            return
        
        lnode = rnode = None
        
        if val < node.val and node.left:
            lnode = self.traverse(node.left, val)
        elif val > node.val and node.right:
            rnode = self.traverse(node.right, val)
        
        return lnode if lnode else rnode
        
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root is None:
            return None

        ans = self.traverse(root, val)
        return ans
# Last updated: 4/21/2025, 10:40:07 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):

        if node:
            self.res.append(node.val)
        
        if node.left:
            self.traverse(node.left)
        if node.right:
            self.traverse(node.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.res = []
        self.traverse(root)
        return self.res
        
        
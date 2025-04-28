# Last updated: 4/28/2025, 4:48:56 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):

        if node.left is None and node.right is None:
            self.res.append(node.val)
            return 

        if node.left:
            self.traverse(node.left)

        self.res.append(node.val)

        if node.right:
            self.traverse(node.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []

        if root is None:
            return self.res

        self.traverse(root)

        return self.res
        
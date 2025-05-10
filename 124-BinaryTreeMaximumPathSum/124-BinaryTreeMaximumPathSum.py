# Last updated: 5/9/2025, 10:50:19 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        print("self.max:", self.max)
        if node.left is None and node.right is None:
            self.max = max(self.max, node.val)
            return node.val

        lval = rval = 0
        if node.left:
            lval= self.traverse(node.left)
        
        if node.right:
            rval = self.traverse(node.right)
        
        total_val = lval + rval + node.val
        l_total = lval + node.val
        r_total = rval + node.val

        self.max = max(self.max, total_val, node.val, l_total, r_total)
        print("self.max:", self.max)
        curr_val = max(l_total, r_total, node.val)
        print("curr_val:", curr_val)

        return curr_val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        self.max = float('-inf')

        self.traverse(root)

        return self.max
        
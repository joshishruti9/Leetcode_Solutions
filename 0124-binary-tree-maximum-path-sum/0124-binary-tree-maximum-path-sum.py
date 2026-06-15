# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):

        if node.left is None and node.right is None:
            self.max_total = max(self.max_total, node.val)
            return node.val

        lval = rval = 0
        if node.left:
            lval = self.traverse(node.left)
        if node.right:
            rval = self.traverse(node.right)
    
        curr_total = lval + rval + node.val
        ltotal = lval + node.val
        rtotal = rval + node.val

        self.max_total = max(self.max_total, curr_total, ltotal, rtotal, node.val)

        return max(ltotal, rtotal, node.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.max_total = float("-inf")
        self.traverse(root)

        return self.max_total
        
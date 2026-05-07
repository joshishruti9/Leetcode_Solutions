# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, curr_sum):
        if node.left is None and node.right is None:
            curr_sum = (curr_sum * 10) + node.val
            return curr_sum
        
        lsum = rsum = 0
        if node.left:
            lsum = self.traverse(node.left, (curr_sum*10) + node.val)
        
        if node.right:
            rsum = self.traverse(node.right, (curr_sum  * 10) + node.val)
        
        return lsum + rsum

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total = self.traverse(root, 0)
        return total
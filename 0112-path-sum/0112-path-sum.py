# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, curr_sum, targetSum):

        if node.left is None and node.right is None:
            if curr_sum + node.val == targetSum:
                return True
            else:
                return False

        left = right = False
        if node.left:
            left = self.traverse(node.left, curr_sum + node.val, targetSum)
        
        if node.right:
            right = self.traverse(node.right, curr_sum + node.val, targetSum)
        
        return left or right
        


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        return self.traverse(root, 0, targetSum)

        
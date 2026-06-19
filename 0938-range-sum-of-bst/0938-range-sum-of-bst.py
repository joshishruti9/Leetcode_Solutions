# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        

        def traverse(node, low, high):
            if node.left is None and node.right is None:
                if low <= node.val <= high:
                    return node.val

            lsum = rsum = 0
            val = node.val if low <= node.val <= high else 0
            
            if node.left:
                lsum = traverse(node.left, low, high)

            if node.right:
                rsum = traverse(node.right, low, high) 

            return lsum + rsum + val

        return traverse(root, low, high)
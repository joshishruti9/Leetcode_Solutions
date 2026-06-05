# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = []

        def traverse(node):
            if node.left is None and node.right is None:
                res.append(node.val)
                return

            if node.left:
                traverse(node.left)
            
            res.append(node.val)

            if node.right:
                traverse(node.right)
            
            return
        
        traverse(root)
        return res[k-1]


        
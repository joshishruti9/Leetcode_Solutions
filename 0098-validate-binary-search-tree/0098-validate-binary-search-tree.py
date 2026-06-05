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
        
        return

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.res = []

        self.traverse(root)

        for i in range(1, len(self.res)):
            if self.res[i-1] >= self.res[i]:
                return False

        return True
        
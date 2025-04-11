# Last updated: 4/10/2025, 10:40:45 PM
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
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = []
        self.traverse(root)
        for i in range(len(self.res)-1):
            if self.res[i] >= self.res[i+1]:
                return False
            print(self.res[i])
        return True
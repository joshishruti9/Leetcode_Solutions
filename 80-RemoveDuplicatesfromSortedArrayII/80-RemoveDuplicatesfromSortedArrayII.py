# Last updated: 4/29/2025, 4:59:16 PM
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
        

        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
       
        self.res = []
        self.diff = float('inf')

        self.traverse(root)

        n = len(self.res)

        for i in range(1,n):
            self.diff = min(self.diff, abs(self.res[i]-self.res[i-1]))

        return self.diff
        
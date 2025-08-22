# Last updated: 8/22/2025, 1:27:55 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, node, p, q):

        flag = rflag = lflag = False

        if node.val == p or node.val == q:
            flag = True

        if node.left is None and node.right is None:
            return flag

        if node.left:
            lflag = self.traverse(node.left, p, q)
        if node.right:
            rflag = self.traverse(node.right, p, q)
        
        if (rflag and lflag) or (rflag and flag) or (lflag and flag):
            self.parent = node
        
        return rflag or lflag or flag 

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root is None:
            return None

        self.parent = None
        
        self.traverse(root, p.val, q.val)

        return self.parent
        
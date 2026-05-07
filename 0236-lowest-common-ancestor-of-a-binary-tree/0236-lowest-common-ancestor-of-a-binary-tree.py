# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, node, p, q):

        flag = rflag = lflag = False

        if node.val == p.val or node.val == q.val:
            flag = True

        if node.left is None and node.right is None:
            return flag
            
        if node.left:
            lflag = self.traverse(node.left, p, q)
        
        if node.right:
            rflag = self.traverse(node.right, p, q)

        
        if (lflag and rflag) or (rflag and flag) or (flag and lflag):
            self.res = node
        
        return lflag or rflag or flag


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return None
        
        self.res = None
        
        self.traverse(root, p, q)

        return self.res

        
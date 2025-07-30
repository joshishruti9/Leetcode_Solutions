# Last updated: 7/30/2025, 4:21:34 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, node, p, q):
        

        l_flag = r_flag = flag = False

        if node.val == p.val or node.val == q.val:
            flag = True
        
        if node.left is None and node.right is None:
            return flag
        
        
        if node.left:
            l_flag = self.traverse(node.left, p, q)
        if node.right:
            r_flag = self.traverse(node.right, p, q)

        if (l_flag and r_flag) or (r_flag and flag) or (l_flag and flag):
            self.lca = node
        
        return l_flag or r_flag or flag

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root is None:
            return None

        self.lca = None
        self.traverse(root, p, q)
        
        return self.lca
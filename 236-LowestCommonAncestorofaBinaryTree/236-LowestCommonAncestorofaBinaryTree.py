# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self,node,p,q):

        rnode = pnode = qnode = False

        if node.val == p.val or node.val == q.val:
            rnode = True

        if node.left is None and node.right is None:
            return rnode

        if node.left:
            pnode = self.traverse(node.left,p,q)
        if node.right:
            qnode = self.traverse(node.right,p,q)

        if (pnode and qnode) or (pnode and rnode) or (qnode and rnode):
            self.lca = node
        
        return pnode or qnode or rnode
        
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        self.lca = None
        self.traverse(root,p,q)
        return self.lca      
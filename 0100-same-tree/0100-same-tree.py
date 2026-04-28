# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, pnode, qnode):
        if pnode is None and qnode is None:
            return True
        
        if pnode is None or qnode is None:
            return False
          
        return pnode.val == qnode.val and self.traverse(pnode.left, qnode.left)    and self.traverse(pnode.right, qnode.right)


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        return self.traverse(p, q)
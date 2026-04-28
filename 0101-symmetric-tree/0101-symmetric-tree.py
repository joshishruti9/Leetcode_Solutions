# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,lnode, rnode):
        if lnode is None and rnode is None:
            return True
        
        if lnode is None or rnode is None:
            return False

        flag = False
        if lnode.val == rnode.val:
            flag = True
        
        
        return flag and self.traverse(lnode.left, rnode.right) and self.traverse(lnode.right, rnode.left)
        

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    
        return self.traverse(root.left, root.right)
        
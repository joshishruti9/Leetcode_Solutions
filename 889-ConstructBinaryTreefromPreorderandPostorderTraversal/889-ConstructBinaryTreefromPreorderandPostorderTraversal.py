# Last updated: 5/20/2025, 5:00:30 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None

        root = TreeNode(val = preorder[0])
        
        if len(preorder) == 1:
            return root
        
        pos = postorder.index(preorder[1])
        root.left = self.constructFromPrePost(preorder[1:pos+2],postorder[:pos+1])
        root.right = self.constructFromPrePost(preorder[pos+2:],postorder[pos+1:])
        
        return root
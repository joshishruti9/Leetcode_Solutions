# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not postorder or not inorder:
            return 

        n = len(postorder)       
        root = TreeNode(val = postorder[n-1])
        index = 0
        while inorder[index] != postorder[n-1]:
            index += 1
        root.left = self.buildTree(inorder[:index],postorder[:index])
        root.right = self.buildTree(inorder[index+1:],postorder[index:n-1])

        return root
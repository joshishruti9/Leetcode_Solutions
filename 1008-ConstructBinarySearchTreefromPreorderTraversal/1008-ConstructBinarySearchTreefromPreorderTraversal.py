# Last updated: 5/26/2025, 4:24:55 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        stack = []
        root = TreeNode(val = preorder[0])
        stack.append(root)
        i = 1

        while i < len(preorder):
            if preorder[i] < stack[-1].val:
                node = stack.pop()
                node.left = TreeNode(val = preorder[i])
                stack.append(node)
                stack.append(node.left) 
                i += 1  
            else:
                while stack and preorder[i] > stack[-1].val:
                    prev_node = stack.pop()
                prev_node.right = TreeNode(val = preorder[i])
                stack.append(prev_node.right)
                i += 1
    
        return root
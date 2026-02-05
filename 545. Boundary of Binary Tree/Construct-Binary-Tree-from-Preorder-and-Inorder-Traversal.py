1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
9
10        if not preorder or not inorder:
11            return None
12
13        node = TreeNode(val = preorder[0]) 
14        i = inorder.index(node.val)
15
16        node.left = self.buildTree(preorder[1:], inorder[:i])     
17        node.right = self.buildTree(preorder[i+1:],inorder[i+1:])
18
19        return node
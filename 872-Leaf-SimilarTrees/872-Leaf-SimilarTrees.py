# Last updated: 4/13/2025, 11:57:27 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, leaf_list):

        if node.left is None and node.right is None:
            leaf_list.append(node.val)
            return

        if node.left:
            self.traverse(node.left, leaf_list)
        if node.right:
            self.traverse(node.right, leaf_list)
        
        return

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if (root1 is None and root2 is not None) or (root2 is None and root1 is not None):
            return False
            
        list1 = []
        list2 = []
        self.traverse(root1, list1)
        self.traverse(root2, list2)

        return list1 == list2
        
# Last updated: 4/13/2025, 12:49:24 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, node_list):
        if node.left is None and node.right is None:
            node_list.append(node.val)
            return

        node_list.append(node.val)

        if node.left:
            self.traverse(node.left, node_list)
        else:
            node_list.append(None)

        if node.right:
            self.traverse(node.right, node_list)
        else:
            node_list.append(None)
            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is not None) or (q is None and p is not None):
            return False
        
        if p is None and q is None:
            return True

        list1 = []
        list2 = []
        self.traverse(p, list1)
        self.traverse(q, list2)
        print(list1)
        print(list2)
        return list1 == list2
        
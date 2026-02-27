1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def traverse(self, node, leaves):
9
10        if node.left is None and node.right is None:
11            leaves.append(node.val)
12            return
13        
14        if node.left:
15            self.traverse(node.left, leaves)
16        
17        if node.right:
18            self.traverse(node.right, leaves)
19        
20
21    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
22
23        if not root1 and not root2:
24            return True
25        
26        if not root1:
27            return False
28        
29        if not root2:
30            return False
31
32        leaves1 = []
33        leaves2 = []
34
35        self.traverse(root1, leaves1)
36        self.traverse(root2, leaves2)
37
38        return leaves1 == leaves2
39
40
41
42        
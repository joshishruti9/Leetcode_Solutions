1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def traverse(self, node, is_boundry, is_left):
9        
10        if node.left is None and node.right is None:
11            self.child.append(node.val)
12            return
13
14        if is_boundry:
15            if is_left:
16                self.left_list.append(node.val)
17            else:
18                self.right_list.append(node.val)
19
20        if node.left:
21            is_left_boundary = is_boundry and (is_left or not node.right)
22            self.traverse(node.left, is_left_boundary, is_left)
23        if node.right:
24            is_right_boundary = is_boundry and (not is_left or not node.left)
25            self.traverse(node.right, is_right_boundary, is_left)
26    
27
28    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
29
30        if not root :
31            return []
32        
33        self.left_list = []
34        self.right_list = []
35        self.child = []
36        
37        if root.left:
38            self.traverse(root.left, True, True)
39        
40        if root.right:
41            self.traverse(root.right, True, False)
42
43        return [root.val] + self.left_list + self.child + self.right_list[::-1]
44
45        
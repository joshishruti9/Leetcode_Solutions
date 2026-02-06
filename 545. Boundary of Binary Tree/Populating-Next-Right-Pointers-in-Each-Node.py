1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
5        self.val = val
6        self.left = left
7        self.right = right
8        self.next = next
9"""
10
11class Solution:
12    
13    def traverse(self, node, is_left, parent_node):
14
15        if is_left:
16            node.next = parent_node.right
17        else:
18            parent_sibling = parent_node.next
19            if parent_sibling:
20                node.next = parent_sibling.left
21        
22        if node.left is None and node.right is None:
23            return
24        
25        if node.left:
26            self.traverse(node.left, True, node)
27        
28        if node.right:
29            self.traverse(node.right, False, node)
30        
31        return
32
33    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
34        #use dfs to avoid extra space. if request for next pointer is coming from left child answer is right child of parent. if request is coming from right child of the tree answer is go to parent do next and then get left child.
35
36        if root is None:
37            return None
38        
39        if root.left:
40            self.traverse(root.left, True, root)
41        if root.right:
42            self.traverse(root.right, False, root)
43
44        return root
45
46
47        
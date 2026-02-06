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
12    def get_next_sibling(self, node, parent_node):
13        while parent_node.next:
14                   
15            parent_node = parent_node.next
16            
17            if parent_node.left:
18                node.next = parent_node.left
19                break
20            elif parent_node.right:
21                node.next = parent_node.right
22                break
23        
24        return 
25
26    def traverse(self, node, is_left, parent_node):
27        
28        if is_left:
29            if parent_node.right: 
30                node.next = parent_node.right
31            else:
32                self.get_next_sibling(node, parent_node) 
33        else:
34            self.get_next_sibling(node, parent_node)
35            
36        
37        if node.left is None and node.right is None:
38            return
39        
40        if node.right:
41            self.traverse(node.right, False, node)
42
43        if node.left:
44            self.traverse(node.left, True, node)
45        
46        return
47
48    def connect(self, root: 'Node') -> 'Node':
49                #use dfs to avoid extra space. if request for next pointer is coming from left child answer is right child of parent. if request is coming from right child of the tree answer is go to parent do next and then get left child.
50
51        if root is None:
52            return None
53
54        if root.right:
55            self.traverse(root.right, False, root)
56        
57        if root.left:
58            self.traverse(root.left, True, root)
59        
60
61        return root
62        
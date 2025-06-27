# Last updated: 6/27/2025, 1:24:23 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def traverse(self, node, level):

        if not node.children:
            self.max_level = max(self.max_level, level)
            return

        if node.children:
            for child in node.children:
                self.traverse(child, level+1)

    def maxDepth(self, root: 'Node') -> int:
        self.max_level = 0

        if root is None:
            return 0
        
        self.traverse(root, 1)

        return self.max_level
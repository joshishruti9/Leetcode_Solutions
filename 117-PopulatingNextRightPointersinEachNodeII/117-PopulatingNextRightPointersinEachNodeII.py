# Last updated: 4/19/2025, 3:12:50 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        queue = [root]

        while queue:
            queue2 = []
            prev_node = queue[0]
            for node in queue: 
                if node is None:
                    continue

                if node.left:
                    queue2.append(node.left)
                
                if node.right:
                    queue2.append(node.right)

                if node != prev_node:
                    prev_node.next = node
                    
                prev_node = node     
            queue = queue2

        return root
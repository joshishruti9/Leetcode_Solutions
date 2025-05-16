# Last updated: 5/15/2025, 8:48:14 PM
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
    def traverse(self, root):
        queue = [root]
        prev_node = ListNode()

        while queue:
            queue2 = []
            for node in queue:
                if node is None:
                    continue
                
                prev_node.next = node
                prev_node = node
            
                if node.left:
                    queue2.append(node.left)
                
                if node.right:
                    queue2.append(node.right)
            
            queue = queue2
            prev_node = ListNode()


        
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        self.traverse(root)

        return root
        
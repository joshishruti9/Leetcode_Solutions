# Last updated: 6/30/2025, 10:29:24 PM
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []

        if root is None:
            return self.res
        
        queue = deque()
        queue.append(root)
        
        while queue:
            queue2 = []
            self.res.append(queue[-1].val)
            for node in queue:
                if node is None:
                    continue
                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
            
            queue = queue2
        
        return self.res
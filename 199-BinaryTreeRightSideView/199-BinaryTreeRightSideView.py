# Last updated: 4/10/2025, 1:20:28 PM
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque()
        queue = [root]

        if root is None:
            return []

        while queue:
            res.append(queue[-1].val)
            queue2 = []
            for node in queue:
                if node is None:
                    continue
                
                if node.left:
                    queue2.append(node.left)
                
                if node.right:
                    queue2.append(node.right)

            queue = queue2

        return res
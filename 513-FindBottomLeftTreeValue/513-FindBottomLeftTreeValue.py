# Last updated: 8/8/2025, 11:01:46 PM
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        queue = [root]
        
        while queue:
            self.ans = queue[0].val
            queue2 = []
            for node in queue:
                if node is None:
                    continue
                
                if node.left:
                    queue2.append(node.left)
                
                if node.right:
                    queue2.append(node.right)
            queue=queue2

        return self.ans
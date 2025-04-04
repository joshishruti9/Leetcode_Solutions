# Last updated: 4/4/2025, 1:54:00 PM
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = deque()
        queue.append(root)
        max_sum = float('-inf')
        total = 0
        level = 1
        while queue:
            queue2 = []
            total = 0
            for node in queue:
                if node is None:
                    continue
                total = total + node.val
                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
            if total > max_sum:
                max_level = level 
            level += 1
            max_sum = max(max_sum, total)
            queue = queue2
        
        return max_level
        
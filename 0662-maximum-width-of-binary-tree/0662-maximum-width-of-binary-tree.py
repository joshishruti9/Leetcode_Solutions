from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()

        if root is None:
            return 0
        
        queue.append((root, 0))
        max_width = 0
        flag = False

        while queue:
            queue2 = []
            max_width = max(max_width, abs(queue[-1][1] - queue[0][1])+1)
            for node, last_level in queue:

                if node.left:
                    queue2.append((node.left, 2 * last_level))
                
                if node.right:
                    queue2.append((node.right, 2 * last_level + 1))
            
            queue = queue2
        
        return max_width

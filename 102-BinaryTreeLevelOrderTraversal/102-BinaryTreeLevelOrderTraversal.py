from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if root is None:
            return res
        
        queue = [root]
        res = []
        while queue:
            queue2 = []
            res2 = []
            for node in queue:
                if node is None:
                    continue
                res2.append(node.val)
                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
            res.append(res2)
            queue = queue2
        return res

        
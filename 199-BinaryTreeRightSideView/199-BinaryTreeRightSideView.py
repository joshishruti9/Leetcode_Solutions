# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        queue = [root]
        res = []
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
        
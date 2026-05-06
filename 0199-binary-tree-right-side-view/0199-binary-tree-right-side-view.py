# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = []

        if not root:
            return res

        queue.append(root)

        while queue:
            queue2 = []
            res.append(queue[-1].val)
            for node in queue:

                if node.left:
                    queue2.append(node.left)
                
                if node.right:
                    queue2.append(node.right)
            
            queue = queue2
        
        return res
        
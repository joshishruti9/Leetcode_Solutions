# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = []

        queue.append(root)

        while queue:
            queue2 = []
            output = []

            for node in queue:

                output.append(node.val)
                
                if node.left:
                    queue2.append(node.left)
                
                if node.right:
                    queue2.append(node.right)
            
            queue = queue2
            res.append(output)

        return res
        
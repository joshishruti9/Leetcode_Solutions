# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []

        queue = [root]

        while queue:
            queue2 = []
            total = 0
            count = 0
            for node in queue:

                total += node.val
                count += 1

                if node.left:
                    queue2.append(node.left)
                
                if node.right:
                    queue2.append(node.right)
            
            res.append(total/count)
            queue = queue2
        
        return res
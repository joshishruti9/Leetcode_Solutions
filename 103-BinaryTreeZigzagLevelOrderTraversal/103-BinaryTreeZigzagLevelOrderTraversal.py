# Last updated: 7/30/2025, 3:44:10 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []

        if root is None:
            return res
        
        level = 1
        queue = [root]

        while queue:
            output = []
            queue2 = []

            for node in queue:
                if node is None:
                    continue
                
                output.append(node.val)

                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
            
            if level % 2 == 0:
                res.append(output[::-1])
            else:
                res.append(output)
            
            level += 1
            queue = queue2
    
        return res
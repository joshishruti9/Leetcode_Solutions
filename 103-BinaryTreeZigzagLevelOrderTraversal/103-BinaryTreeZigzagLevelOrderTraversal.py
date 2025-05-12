# Last updated: 5/11/2025, 6:29:19 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        
        queue = []
        queue.append(root)
        queue2 = []
        level = 1
        res = []


        while queue:  
            queue2 = []
            output = []
            for node in queue:
                if node is None:
                    continue
                
                output.append(node.val)
                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
                    
            if level%2 != 0:
                res.append(output)
            else:
                res.append(output[::-1])
            level += 1
            queue = queue2
        
        return res
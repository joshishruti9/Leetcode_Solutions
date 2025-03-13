from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        count = 1
        res = []
        if root is None:
            return res

        queue = [root]

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

            queue = queue2
            if (count % 2 == 0):
                res.append(output[::-1])
            else:
                res.append(output)
            count += 1
        return res       
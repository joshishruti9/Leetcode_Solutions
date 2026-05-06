# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = []
        res = []

        if not root:
            return res

        level = 0
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
            if level % 2 == 0:
                res.append(output)
            else:
                res.append(output[::-1])
            level += 1

        return res
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        count = 1

        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            output = []
            queue2 = []

            for node in queue:

                output.append(node.val)

                if node.left:
                    queue2.append(node.left)
                
                if node.right:
                    queue2.append(node.right)

            if count % 2 == 0:
                res.append(output[::-1])
            else:
                res.append(output)

            count += 1
            queue = queue2
        
        return res
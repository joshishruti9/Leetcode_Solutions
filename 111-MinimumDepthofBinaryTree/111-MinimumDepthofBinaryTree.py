# Last updated: 4/19/2025, 2:20:31 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        queue = []
        curr_length = 1
        queue.append(root)

        while queue:
            queue2 = []
            
            for node in queue:
                left_flag = right_flag = False
                if node is None:
                    continue

                print(node.val)

                if node.left:
                    queue2.append(node.left)
                else:
                    left_flag = True

                if node.right:
                    queue2.append(node.right)
                else:
                    right_flag = True
                
                if right_flag and left_flag:
                    print(curr_length," ",node.val)
                    return curr_length

            queue = queue2 
            curr_length += 1

        return curr_length      
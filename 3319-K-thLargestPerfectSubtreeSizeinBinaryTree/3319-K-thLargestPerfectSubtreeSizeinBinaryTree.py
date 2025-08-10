# Last updated: 8/9/2025, 11:46:21 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        if node.left is None and node.right is None:
            self.res.append(1)
            return (1, True)
        
        lflag = rflag = flag = False
        lcount = rcount = 0
        if node.left:
            lcount, lflag = self.traverse(node.left)
        
        if node.right:
            rcount, rflag = self.traverse(node.right)
        
        if lcount == rcount and lflag and rflag:
            self.res.append(lcount+rcount+1)
            flag = True
        
        return (lcount+rcount+1, flag)

            
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0

        self.res = []

        self.traverse(root)
        nums = sorted(self.res, reverse = True)

        print(nums)

        if len(nums) < k:
            return -1

        return nums[k-1]
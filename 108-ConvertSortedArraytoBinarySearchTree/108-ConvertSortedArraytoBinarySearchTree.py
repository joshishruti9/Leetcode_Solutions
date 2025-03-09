# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        n = len(nums)
        root_index = n // 2
        node = TreeNode(val = nums[root_index])
        lnode = self.sortedArrayToBST(nums[:root_index])
        rnode = self.sortedArrayToBST(nums[root_index+1:])
        node.left = lnode
        node.right = rnode
        
        return node
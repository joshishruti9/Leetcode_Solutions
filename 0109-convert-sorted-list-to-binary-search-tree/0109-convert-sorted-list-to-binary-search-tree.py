# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def create_tree(self, nums, start, end):
        if start > end:
            return None

        mid = (start + end) // 2

        root_node = TreeNode(nums[mid]) 

        root_node.left = self.create_tree(nums, start, mid-1)
        root_node.right = self.create_tree(nums, mid+1, end)

        return root_node


    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        
        nums = []
        node = head

        while node:
            nums.append(node.val)
            node = node.next
        
        return self.create_tree(nums, 0, len(nums)-1)
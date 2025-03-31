# Last updated: 3/30/2025, 5:53:44 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev_node = head
        node = prev_node.next

        while node:
            temp = node.next
            node.next = prev_node
            prev_node = node
            node = temp

        head.next = None
        return prev_node
        
        
        
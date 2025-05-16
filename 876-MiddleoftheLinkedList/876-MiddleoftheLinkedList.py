# Last updated: 5/16/2025, 3:00:38 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0

        node = head

        while node:
            length += 1
            node = node.next

        count = 0
        node = head
        while node:
            if count == (length // 2):
                return node
            
            count += 1
            node = node.next


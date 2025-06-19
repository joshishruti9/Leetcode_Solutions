# Last updated: 6/18/2025, 9:20:38 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        n = 0

        node = head
        while node:
            n += 1
            node = node.next
        
        count = 0
        node = head

        while count != n//2:
            count += 1
            node = node.next
        
        return node
        
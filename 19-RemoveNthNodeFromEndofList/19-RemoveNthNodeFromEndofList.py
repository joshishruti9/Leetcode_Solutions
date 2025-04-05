# Last updated: 4/5/2025, 4:22:03 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        psudeo_head = ListNode()
        psudeo_head.next = head
        node = head
        
        length = 0
        while node:
            node = node.next
            length += 1
        
        n = length - n

        length = 0
        node = psudeo_head

        while length != n:
            node = node.next
            length += 1

        if node.next:
            node.next = node.next.next

        return psudeo_head.next
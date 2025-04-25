# Last updated: 4/24/2025, 5:36:07 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        psuedo_head = ListNode()
        node = ListNode()
        psuedo_head.next = node
        node = head
        prev_node = psuedo_head

        while node:
            if prev_node.val == node.val and psuedo_head != prev_node:
                node = node.next
            else:
                prev_node.next = node
                prev_node = prev_node.next
                node = node.next
        
        prev_node.next = None
        return psuedo_head.next
# Last updated: 6/5/2025, 2:54:30 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        psudeo_head = ListNode()
        prev_node = psudeo_head
        node = head

        while node and node.next:
            
            first = node
            second = node.next

            #swap
            prev_node.next = second
            first.next = second.next
            second.next = first

            prev_node = first
            node = first.next

        return psudeo_head.next
            
        

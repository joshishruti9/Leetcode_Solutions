# Last updated: 5/20/2025, 2:24:52 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        
        if not head.next:
            return head
        
        psuedo_head = ListNode()
        psuedo_head.next = head

        prev_prev_node = psuedo_head
        prev_node = head
        node = prev_node.next

        while node:
            if prev_node.val == node.val:
                while node and prev_node.val == node.val:
                    node = node.next
                prev_prev_node.next = node
                prev_node = node
                if node:
                    node = node.next
            else:
                prev_prev_node = prev_prev_node.next
                prev_node = node
                node = node.next
    
        return psuedo_head.next     
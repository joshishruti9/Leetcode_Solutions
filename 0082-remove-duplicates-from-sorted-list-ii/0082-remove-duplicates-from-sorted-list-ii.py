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
        prev_node = psuedo_head
        prev_node.next = head
        curr_node = head
        next_node = head.next

        while next_node:
            if curr_node.val == next_node.val:
                while next_node and curr_node.val == next_node.val:
                    next_node = next_node.next
                
                prev_node.next = next_node
                curr_node = next_node
                
                if next_node:
                    next_node = next_node.next

            else:
                prev_node = prev_node.next
                curr_node = curr_node.next
                next_node = next_node.next
        
        return psuedo_head.next
        
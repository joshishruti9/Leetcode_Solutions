# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right or not head or not head.next:
            return head

        count = 1
        node = head
        psuedo_head = ListNode()
        prev_node = psuedo_head

        while count != left:
            prev_node.next = node
            prev_node = node
            node = node.next
            count += 1
        
        prev_left = prev_node
        left = node
        prev_node = node
        node = node.next

        while count != right:
            temp_node = node.next
            node.next = prev_node
            prev_node = node
            node = temp_node
            count += 1

        left.next = node

        if prev_left:
            prev_left.next = prev_node
        
        return psuedo_head.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        if not head:
            return None

        fake_head = ListNode()
        prev_node = fake_head

        node = head

        while node and node.val < x:
            
            prev_node.next = node
            prev_node = node

            node = node.next  

        prev_big_node = prev_node
        big_node = node

        if node is None:
            return head

        while node:
            if node.val < x:
                temp_node = node.next
                prev_big_node.next = node
                node.next = big_node
                prev_big_node = node
                prev_node.next = temp_node
                node = temp_node
                
            else:   
                prev_node.next = node
                prev_node = prev_node.next
                node = node.next   

        return fake_head.next  
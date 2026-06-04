# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # We will compare curr_node val to prev_node value if it is same we will join prev_node to next_node of curr_node 

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        fake_head = ListNode()
        prev_node = fake_head
        node = head

        while node and node.next:
            if node.val != node.next.val:
                prev_node.next = node
                prev_node = node 
                node = node.next
            else:
                while node.next and node.val == node.next.val:
                    node = node.next
                prev_node.next = node.next
                node.next = None
                node = prev_node.next

        return fake_head.next
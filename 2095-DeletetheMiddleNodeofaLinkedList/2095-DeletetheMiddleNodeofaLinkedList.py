# Last updated: 3/30/2025, 5:31:07 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev_odd_head = ListNode()
        prev_even_head = ListNode()
        curr_even = prev_even_head
        curr_odd = prev_odd_head

        node = head
        count  = 0

        while node:
            if (count % 2) == 0:
                curr_odd.next = node
                curr_odd = curr_odd.next
            else:
                curr_even.next = node
                curr_even = curr_even.next
            count += 1
            node = node.next
        curr_even.next = None
        curr_odd.next = prev_even_head.next

        return prev_odd_head.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        if not head:
            return None

        fake_head_small = ListNode()
        fake_head_big = ListNode()

        fake_small = fake_head_small
        fake_big = fake_head_big

        node = head

        while node:
            if node.val < x:
                fake_head_small.next = node
                fake_head_small = fake_head_small.next
            else:
                fake_head_big.next = node
                fake_head_big = fake_head_big.next

            node = node.next
        
        fake_head_big.next = None
        fake_head_small.next = fake_big.next

        return fake_small.next

        
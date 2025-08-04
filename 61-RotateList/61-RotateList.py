# Last updated: 8/4/2025, 4:07:51 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None:
            return None
        
        n = 0
        node = head

        while node:
            n += 1
            node = node.next
        
        k = k % n

        if k == 0:
            return head

        count = 0
        node = head

        while count < n-k-1:
            node = node.next
            count += 1
        
        new_head = node.next
        node.next = None

        node = new_head

        while node.next:
            node = node.next
        
        node.next = head

        return new_head
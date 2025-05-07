# Last updated: 5/6/2025, 11:27:54 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count  = 0
        n = 0
        node = head

        if head is None:
            return None

        while node:
            n += 1
            node = node.next

        k = k % n

        if k == 0:
            return head

        psuedo_head = ListNode()
        node = head

        while count < n-k-1:
            count += 1
            node = node.next
        
        psuedo_head.next = node.next
        node.next = None


        node = psuedo_head.next

        while node.next:
            node = node.next

        node.next = head

        return psuedo_head.next        
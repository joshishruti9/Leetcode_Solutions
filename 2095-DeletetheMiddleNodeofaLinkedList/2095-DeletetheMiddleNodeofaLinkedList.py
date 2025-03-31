# Last updated: 3/30/2025, 5:07:38 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
            
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
            
        mid = n // 2

        node = head
        count = 1
        while node:
            if count == mid:
                node.next = node.next.next
                break
            else:
                node = node.next
            count += 1

        return head
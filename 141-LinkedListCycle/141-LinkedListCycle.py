# Last updated: 5/16/2025, 4:22:01 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return None
        
        slow = head
        fast = head.next

        while fast and fast.next:

            if slow == fast:
                return True
            
            slow = slow.next
            fast = fast.next.next

        return False
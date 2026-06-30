# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        slow = head
        fast = head
        is_cycle = False

        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                is_cycle = True
                break
        
        if not is_cycle:
            return None
        
        slow = head
        while slow != fast:

            fast = fast.next
            slow = slow.next
        
        return slow

        
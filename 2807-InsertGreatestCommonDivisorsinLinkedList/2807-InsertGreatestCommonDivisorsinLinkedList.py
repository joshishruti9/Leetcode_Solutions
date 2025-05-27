# Last updated: 5/27/2025, 3:02:09 PM
import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        

        node = head

        while node.next:
            val1 = node.val
            val2 = node.next.val
            gcd_val = math.gcd(val1,val2)

            new_node = ListNode(val = gcd_val)

            temp = node.next
            node.next = new_node
            new_node.next = temp

            node = new_node.next
        
        return head
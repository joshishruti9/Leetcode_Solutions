# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None:
            return None
        
        count = 0
        node = head

        while node:
            count += 1
            node = node.next
        
        k = k % count

        if k == 0:
            return head

        n = count - k
        count = 1
        node = head

        while count != n:
            count += 1
            node = node.next
        
        temp_node = node.next
        node.next = None

        node = temp_node

        while node.next:
            node = node.next
        
        node.next = head

        return temp_node
        
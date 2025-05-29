# Last updated: 5/29/2025, 1:53:46 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None

        psudeo_head = ListNode()

        stack = deque()
        node = head
        prev_node = psudeo_head
        
        while node:
            if stack and node.val > stack[-1].val:
                stack.pop()
            else:
                stack.append(node)
                node = node.next
        
        while stack:
            node = stack.popleft()
            prev_node.next = node
            prev_node = node
        
        prev_node.next = None

        return psudeo_head.next
# Last updated: 5/4/2025, 2:25:20 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def sort_func(t):
            # t = (node, node_val)
            return t[1]

        nodes = dict()

        if head is None:
            return None

        node = head

        while node:
            nodes[node] = node.val
            node = node.next
        
        sorted_map = sorted(nodes.items(), key = sort_func)

        psuedo_head = ListNode()
        prev_node = psuedo_head

        for value, key in sorted_map:
            prev_node.next = value
            prev_node = value
        prev_node.next = None
        
        return psuedo_head.next
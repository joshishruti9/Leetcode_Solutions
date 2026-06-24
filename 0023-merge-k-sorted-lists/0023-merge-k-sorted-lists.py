from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None
        
        num_queue = []
        
        for i in range(len(lists)):
            if lists[i]:
                heappush(num_queue, (lists[i].val, i, lists[i]))
        
        fake_head = ListNode()
        prev_node = fake_head
        
        while num_queue:
            node_val, index, node = heappop(num_queue)
            prev_node.next = node
            prev_node = node

            if node.next:
                heappush(num_queue, (node.next.val, index, node.next))
        
        return fake_head.next

        
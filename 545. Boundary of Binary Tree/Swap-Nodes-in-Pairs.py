1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head or not head.next:
9            return head
10        
11        pseudo_head = ListNode(val = None, next = head)
12
13        prev_node = pseudo_head
14        curr_node = pseudo_head.next
15    
16        while curr_node and curr_node.next:
17
18            #swap
19            temp_node = curr_node.next
20            prev_node.next = temp_node
21            curr_node.next = temp_node.next
22            temp_node.next = curr_node
23            
24            prev_node = curr_node
25            curr_node = curr_node.next
26        
27        return pseudo_head.next
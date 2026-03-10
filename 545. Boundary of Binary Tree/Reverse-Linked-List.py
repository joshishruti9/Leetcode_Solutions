1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8
9        if not head or not head.next:
10            return head
11        
12        prev_node = head
13        curr_node = head.next
14        prev_node.next = None
15    
16        while curr_node:
17            temp = curr_node.next
18            curr_node.next = prev_node
19        
20            prev_node = curr_node
21            curr_node = temp
22        
23
24        return prev_node
25
26
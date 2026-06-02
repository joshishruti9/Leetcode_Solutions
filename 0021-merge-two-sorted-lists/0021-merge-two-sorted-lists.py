# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        node1 = list1
        node2 = list2

        psudo_head = ListNode()
        prev_node = psudo_head


        while node1 and node2:

            if node1.val <= node2.val:
                prev_node.next = node1
                node1 = node1.next
            else:
                prev_node.next = node2
                node2 = node2.next
            
            prev_node = prev_node.next
        
        if node1:
            prev_node.next = node1
            prev_node = prev_node.next
            node1 = node1.next
        
        if node2:
            prev_node.next = node2
            prev_node = prev_node.next
            node2 = node2.next
        
        return psudo_head.next



        
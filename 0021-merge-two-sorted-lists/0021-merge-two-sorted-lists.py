# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None

        node1 = list1
        node2 = list2

        psuedo_head = ListNode()
        prev = psuedo_head

        while node1 and node2:
            if node1.val <= node2.val:
                prev.next = node1
                node1 = node1.next
            else:
                prev.next = node2
                node2 = node2.next
            
            prev = prev.next
        
        node = node1 if node1 else node2

        while node:
            prev.next = node
            prev = node
            node = node.next

        return psuedo_head.next
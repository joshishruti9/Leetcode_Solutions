# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        set_A = set()

        node_A = headA 
        node_B = headB

        while node_A:
            set_A.add(node_A)
            node_A = node_A.next

        while node_B:
            if node_B in set_A:
                return node_B
            node_B = node_B.next

        return None     
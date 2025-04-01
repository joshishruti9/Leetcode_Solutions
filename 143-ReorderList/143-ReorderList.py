# Last updated: 4/1/2025, 2:25:24 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        visited = []

        node = head

        while node:
            visited.append(node)
            node = node.next

        p1 = 0
        p2 = len(visited) - 1
        prev_node = ListNode()
        node = prev_node

        while p1 <= p2:
            prev_node.next = visited[p1]
            prev_node = prev_node.next
            prev_node.next = visited[p2]
            prev_node = prev_node.next
            p1 += 1
            p2 -= 1
        prev_node.next = None
        return node.next
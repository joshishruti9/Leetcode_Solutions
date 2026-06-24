# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        nums = []

        node = head

        while node:
            nums.append(node.val)
            node = node.next
        
        nums.sort()
        fake_head = ListNode()
        prev_node = fake_head

        for num in nums:
            node = ListNode(num)
            prev_node.next = node
            prev_node = node
            node = node.next
        
        return fake_head.next

        
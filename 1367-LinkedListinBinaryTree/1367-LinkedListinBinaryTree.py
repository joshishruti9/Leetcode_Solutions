# Last updated: 5/15/2025, 9:20:26 PM

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:

        node = head
        num = []

        while node:
            num.append(str(node.val)) 
            node = node.next
        
        return int("".join(num),2)
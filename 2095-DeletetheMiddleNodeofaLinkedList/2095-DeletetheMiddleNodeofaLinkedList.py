# Last updated: 3/30/2025, 5:38:43 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        n = 0
        arr = []

        while head:
            n += 1
            arr.append(head.val)
            head = head.next
        
        max_sum = 0
        p1 = 0
        p2 = n-1

        while p1 < p2:
            max_sum = max(max_sum, (arr[p1] + arr[p2]))
            p1 += 1
            p2 -= 1
        
        return max_sum
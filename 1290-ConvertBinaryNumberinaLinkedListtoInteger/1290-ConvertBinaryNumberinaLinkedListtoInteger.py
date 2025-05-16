# Last updated: 5/15/2025, 10:03:35 PM

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def convert_binary(self, num):
        count = 0
        bin_num = 0

        while num > 0:
            digit = num % 10
            bin_num = digit * (2 ** count) + bin_num
            num = num//10
            count += 1

        return bin_num

    def getDecimalValue(self, head: Optional[ListNode]) -> int:

        node = head
        num = 0
        count = 0

        while node:
            num = (num * 2) + node.val
            node = node.next
            count += 1
        
        return num
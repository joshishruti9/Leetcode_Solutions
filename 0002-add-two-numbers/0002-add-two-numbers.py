# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def create_list(self, num):
        psuedo_head = ListNode()
        prev = psuedo_head

        while num > 0:
            node = ListNode(num % 10)
            prev.next = node
            prev = prev.next
            num = num // 10
        
        return psuedo_head.next

    def create_num(self, node):
        
        num = 0
        count = 0

        while node:
            num += (node.val) * (10 ** count)
            count += 1
            node = node.next
        
        return num

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1 = self.create_num(l1)
        num2 = self.create_num(l2)

        if num1+num2 == 0:
            return ListNode(val=0)

        node = self.create_list(num1+num2)

        return node


        
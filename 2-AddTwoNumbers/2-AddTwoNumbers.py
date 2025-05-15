# Last updated: 5/15/2025, 4:45:26 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def make_num(self, linked_list):
        node = linked_list
        count = 0
        num = 0
        while node:
            num = num + (10 ** count) * (node.val)
            node = node.next
            count += 1
        return num
    
    def make_ll(self, num):
        psudeo_head = ListNode()
        prev_node = psudeo_head

        while num > 0:
            number = num % 10
            node = ListNode(val = number)
            prev_node.next = node
            prev_node = node
            num = num // 10
        
        prev_node.next = None
        return psudeo_head.next


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1 and not l2:
            return None

        num1 = self.make_num(l1)
        num2 = self.make_num(l2)

        if num1+num2 == 0:
            return ListNode(val=0)

        head = self.make_ll(num1+num2)

        return head
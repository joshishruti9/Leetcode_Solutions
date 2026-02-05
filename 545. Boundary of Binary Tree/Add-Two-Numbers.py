1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def create_LL(self, num):
8        head = ListNode(num % 10)
9        prev = head
10
11        num = num // 10
12
13        while num > 0:
14            digit = num % 10
15            node = ListNode(digit)
16            prev.next = node
17            prev = node
18            num = num // 10
19        
20        return head
21
22    def create_num(self, node):
23        num = 0
24        count = 0
25        while node:
26            num = num + node.val * (10 ** count)
27            node = node.next
28            count += 1
29        
30        return num
31
32    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
33
34        if l1 is None and l2 is None:
35            return None
36        
37        if l1 is None:
38            return l2
39        
40        if l2 is None:
41            return l1
42
43        num1 = 0
44        num2 = 0
45
46        num1 = self.create_num(l1)
47        num2 = self.create_num(l2)
48
49        return self.create_LL(num1+num2)
50
51        
52        
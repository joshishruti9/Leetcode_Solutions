1class Node:
2    def __init__(self, val, next=None):
3        self.val = val
4        self.next = next
5
6class MyCircularQueue:
7
8    def __init__(self, k: int):
9        self.front = None
10        self.end = None
11        self.size = k
12        self.curr_size = 0
13        
14
15    def enQueue(self, value: int) -> bool:
16        if self.isFull():
17            return False
18
19        new_node = Node(value)
20
21        if self.curr_size == 0:
22            #i.e self.front = self.en. so we will add node to end and make
23            self.front = new_node
24        else:
25            self.end.next = new_node
26
27        self.end = new_node
28        self.curr_size += 1
29        return True
30
31    def deQueue(self) -> bool:
32        if self.isEmpty():
33            return False
34
35        self.front = self.front.next
36        self.curr_size -= 1
37        if self.curr_size == 0:
38            self.front = self.end
39        
40        return True
41
42    def Front(self) -> int:
43        if self.isEmpty():
44            return -1
45        else:
46            return self.front.val 
47        
48
49    def Rear(self) -> int:
50        if self.isEmpty():
51            return -1
52        else:
53            return self.end.val
54        
55
56    def isEmpty(self) -> bool:
57        if self.curr_size == 0:
58            return True
59        else:
60            return False
61        
62
63    def isFull(self) -> bool:
64        if self.curr_size == self.size:
65            return True
66        else:
67            return False
68        
69
70
71# Your MyCircularQueue object will be instantiated and called as such:
72# obj = MyCircularQueue(k)
73# param_1 = obj.enQueue(value)
74# param_2 = obj.deQueue()
75# param_3 = obj.Front()
76# param_4 = obj.Rear()
77# param_5 = obj.isEmpty()
78# param_6 = obj.isFull()
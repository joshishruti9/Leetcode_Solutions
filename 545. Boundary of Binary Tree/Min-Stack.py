1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        
6        
7
8    def push(self, val: int) -> None:
9        if not self.stack:
10            self.stack.append((val, val))
11        else:
12            min_val = min(self.stack[-1][1], val) 
13            self.stack.append((val, min_val))
14                
15    def pop(self) -> None:
16        self.stack.pop(-1)
17
18    def top(self) -> int:
19        if self.stack:
20            return self.stack[-1][0]
21
22    def getMin(self) -> int:
23        return self.stack[-1][1]
24        
25
26
27# Your MinStack object will be instantiated and called as such:
28# obj = MinStack()
29# obj.push(val)
30# obj.pop()
31# param_3 = obj.top()
32# param_4 = obj.getMin()
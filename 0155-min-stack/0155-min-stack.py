class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = float("inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
            self.curr_min = val
        else:
            self.curr_min = min(val, self.curr_min)
            self.stack.append([val, self.curr_min])
        
    def pop(self) -> None:
        if self.stack:
            element, last_min = self.stack.pop()
            if self.curr_min == last_min:
                if self.stack:
                    self.curr_min = self.stack[-1][1]

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        
    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
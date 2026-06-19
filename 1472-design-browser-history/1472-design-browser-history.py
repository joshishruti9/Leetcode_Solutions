class BrowserHistory:

    def __init__(self, homepage: str):
        self.browerHistory = []
        self.browerHistory.append(homepage)
        self.curr_index = 0

    def visit(self, url: str) -> None:
        if self.browerHistory[self.curr_index] == self.browerHistory[-1]:
            self.browerHistory.append(url)      
        else:
            while self.browerHistory[self.curr_index] != self.browerHistory[-1]:
                self.browerHistory.pop()
            self.browerHistory.append(url)
        self.curr_index += 1  
        
    def back(self, steps: int) -> str:
        if self.curr_index - steps < 0:
            self.curr_index = 0
            return self.browerHistory[0]
        else:
            self.curr_index = self.curr_index - steps
            return self.browerHistory[self.curr_index]
        

    def forward(self, steps: int) -> str:
        if len(self.browerHistory) <= steps + self.curr_index:
            self.curr_index = len(self.browerHistory) - 1
            return self.browerHistory[-1]
        else:
            self.curr_index = self.curr_index + steps
            return self.browerHistory[self.curr_index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
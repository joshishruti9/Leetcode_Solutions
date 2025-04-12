# Last updated: 4/12/2025, 3:34:51 PM
from collections import deque

class RecentCounter:
    
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        count = 0
        self.queue.append(t)
        range_start = t - 3000
        range_end = t

        while self.queue and range_start > self.queue[0]:
            self.queue.popleft()
        
        return len(self.queue)
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
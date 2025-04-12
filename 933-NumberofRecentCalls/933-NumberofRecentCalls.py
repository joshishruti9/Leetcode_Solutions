# Last updated: 4/12/2025, 3:26:56 PM
from collections import deque
class RecentCounter:
    
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        count = 0
        self.queue.append(t)
        range_start = t - 3000
        range_end = t

        for val in self.queue:
            if range_start <= val <= range_end:
                count += 1
        
        return count
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
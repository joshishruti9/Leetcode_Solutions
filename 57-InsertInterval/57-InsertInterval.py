# Last updated: 7/23/2025, 6:34:13 PM
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
    
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
            
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval  # move current interval into merge position
            
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        res.append(newInterval)
        
        return res

        
        
        
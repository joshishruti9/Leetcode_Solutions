# Last updated: 7/23/2025, 6:26:50 PM
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        new_list = [newInterval,[float("inf"),float("inf")]]

        
        intervals.append([float("inf"),float("inf")])

        p1 = 0
        p2 = 0

        while p1 < len(intervals) and p2 < len(new_list):
            if intervals[p1][0] < new_list[p2][0]:
                if res:
                    if res[-1][1] >= intervals[p1][0]:
                        start = min(res[-1][0], intervals[p1][0])
                        end = max(res[-1][1], intervals[p1][1])
                        res.pop()
                        res.append([start, end])
                    else:
                        res.append([intervals[p1][0],intervals[p1][1]])
                else:
                    res.append([intervals[p1][0],intervals[p1][1]])
                p1 += 1
            else:
                if res:
                    if res[-1][1] >= new_list[p2][0]:
                        start = min(res[-1][0], new_list[p2][0])
                        end = max(res[-1][1], new_list[p2][1])
                        res.pop()
                        res.append([start, end])
                    else:
                        res.append([new_list[p2][0],new_list[p2][1]])
                else:
                    res.append([new_list[p2][0],new_list[p2][1]])
                p2 += 1
            
        return res[:-1]
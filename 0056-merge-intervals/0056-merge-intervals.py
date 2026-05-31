class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        j = 1
        res = []
        intervals.sort()
        res.append(intervals[0])


        while j < len(intervals):
            if res[-1][1] >= intervals[j][0]:
                start, end = res.pop()
                res.append([min(start, intervals[j][0]), max(intervals[j][1], end)])
            else:
                res.append([intervals[j][0], intervals[j][1]])
            
            j += 1
        
        return res

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        res = [intervals[0]]
        i = 1

        while i < len(intervals):
            if ((res[-1][1] <= intervals[i][1]) and (intervals[i][0] <= res[-1][0])) or ((res[-1][1] >= intervals[i][1]) and (intervals[i][0] >= res[-1][0])):
                min_num = min(intervals[i][0], res[-1][0])
                max_num = max(intervals[i][1], res[-1][1])
                res.pop()
                res.append([min_num, max_num])
                i += 1
            else:
                res.append([intervals[i][0], intervals[i][1]])
                i += 1
        
        print(res)
        return len(res)


        
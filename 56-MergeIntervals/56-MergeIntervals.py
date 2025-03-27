# Last updated: 3/26/2025, 11:16:53 PM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start, end = intervals[0]
        result = []

        for i in range(1,len(intervals)):
            new_start, new_end = intervals[i]
            if end >= new_start:
                end = max(new_end,end)
            else:
                result.append([start,end])
                start, end = new_start, new_end
        result.append([start,end])
        return result
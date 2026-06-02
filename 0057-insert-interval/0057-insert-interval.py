class Solution:
    # we can one res list which will be our output
    # we will put first interval from intervals in res
    # we will start loop and compare last res interval with curr_interval from intervals, if we can merge them pop last interval from res and add merged interval else add curr_interval
    # after adding interval compare last res with new_interval and similarly if we can merge, pop and add merged interval or else add new_interval if it fits there

    # we will merge interval if res[-1][1] >= new_interval[1][0] or curr_interval[j][0]


    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        if len(intervals) == 0:
            return [newInterval]

        isNewIntervalUnused = True

        if intervals[0][0] > newInterval[0]:
            res.append([newInterval[0], newInterval[1]])
            j = 0
            isNewIntervalUnused = False
        else:
            res.append([intervals[0][0],intervals[0][1]])
            j = 1

        while j < len(intervals):
            if isNewIntervalUnused:
                if intervals[j][0] <= newInterval[0]:
                    if res[-1][1] >= intervals[j][0]:
                        start, end = res.pop()
                        res.append([min(start, intervals[j][0]), max(end, intervals[j][1])])
                    else:
                        res.append([intervals[j][0], intervals[j][1]])
                    j += 1
                else:
                    if res[-1][1] >= newInterval[0]:
                        start, end = res.pop()
                        res.append([min(start, newInterval[0]), max(end, newInterval[1])])
                        isNewIntervalUnused = False
                    else:
                        res.append([newInterval[0], newInterval[1]])
            else:
                #just check intervals                   
                if res[-1][1] >= intervals[j][0]:
                    start, end = res.pop()
                    res.append([min(start, intervals[j][0]), max(end, intervals[j][1])])
                else:
                    res.append([intervals[j][0], intervals[j][1]])
                
                j += 1
        
        if isNewIntervalUnused:
            if res[-1][1] >= newInterval[0]:
                start, end = res.pop()
                res.append([min(start, newInterval[0]), max(end, newInterval[1])])
                isNewIntervalUnused = False
            else:
                res.append([newInterval[0], newInterval[1]])

        return res


        


        
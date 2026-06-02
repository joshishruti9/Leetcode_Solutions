class Solution:

    def update(self, res, target_interval):
        src_interval = res[-1]
        if target_interval[0] <= src_interval[1]:
            # src = [1,10] target = [5,15]
            res[-1][1] = max(src_interval[1], target_interval[1])
        else:
            # src = [1,10] target = [11,15]
            res.append(target_interval)

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        if len(intervals) == 0:
            return [newInterval]

        # make first choice
        first_interval = intervals[0]
        if first_interval[0] < newInterval[0]:
            res.append(first_interval)
            j = 1
        else:
            res.append(newInterval)
            j = 0
        
        is_new_interval_inserted = False

        # loop over intervals
        while j < len(intervals):
            candidate_intervals = [intervals[j]]
            if not is_new_interval_inserted:
                candidate_intervals.append(newInterval)
            target_interval = min(candidate_intervals)
            self.update(res, target_interval)
            if not is_new_interval_inserted and target_interval == newInterval:
                is_new_interval_inserted = True
            else:
                j += 1

        if not is_new_interval_inserted:
            self.update(res, newInterval)
        
        return res
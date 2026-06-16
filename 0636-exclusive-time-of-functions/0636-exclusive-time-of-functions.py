class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        output = [0 for i in range(n)]
    
        stack = []
        log_list = logs[0].split(":")
        stack.append([log_list[0], log_list[1], log_list[2]])
        
        for i in range(1, len(logs)):
            curr_log = logs[i].split(":")
            curr_id, curr_state, curr_time = curr_log
            curr_time = int(curr_time)
            curr_id = int(curr_id)
                  
            if curr_state == "start":
                  stack.append(curr_log)
                  continue

            if stack[-1][1] == "diff":
                diff_id, diff_state, curr_diff_time = stack.pop()
                start_id, start_state, start_time = stack.pop()
                start_time = int(start_time)
                time_diff = curr_time - start_time + 1

                updated_diff_time = time_diff - curr_diff_time
                output[curr_id] += updated_diff_time
            else:
                start_id, start_state, start_time = stack.pop()
                start_time = int(start_time)
                time_diff = curr_time - start_time + 1
                output[curr_id] += time_diff
            
            if stack:
                if stack[-1][1] == "diff":
                    stack[-1][2] += time_diff
                else:
                    stack.append([curr_id, "diff", time_diff])
            
        return output

        
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        output = [0 for i in range(n)]
    
        stack = []
        log_list = logs[0].split(":")
        stack.append([log_list[0], log_list[1], log_list[2]])
        
        for i in range(1, len(logs)):
            log_list = logs[i].split(":")
                  
            if log_list[1] == "start":
                  stack.append(log_list)
            else:
                if stack[-1][1] == "diff":
                    diff_log = stack.pop()
                    past_log_list = stack.pop()
                    time_diff = int(log_list[2]) - int(past_log_list[2]) + 1
                    updated_time = time_diff - diff_log[2]
                    output[int(log_list[0])] += updated_time
                else:
                    past_log_list = stack.pop()
                    time_diff = int(log_list[2]) - int(past_log_list[2]) + 1
                    output[int(log_list[0])] += time_diff
                
                if stack:
                    if stack[-1][1] == "diff":
                        stack[-1][2] += time_diff
                    else:
                        stack.append([past_log_list[0], "diff", time_diff])
            
        return output

        
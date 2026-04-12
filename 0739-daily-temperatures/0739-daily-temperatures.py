class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        curr_temp = 0
        res = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                num = stack.pop()
                res[num] = i - num
            else:
                stack.append(i)
        
        return res

        
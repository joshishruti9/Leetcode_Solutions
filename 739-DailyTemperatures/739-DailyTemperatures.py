# Last updated: 8/18/2025, 11:09:22 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0 for i in range(len(temperatures))]
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                item = stack.pop()
                res[item] = i - item
            stack.append(i)
              
        return res
        
# Last updated: 3/29/2025, 4:46:25 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        min_stack = []
        result = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            while min_stack and temperatures[min_stack[-1]] < temperatures[i]:
                item = min_stack.pop()
                result[item] = i - item
            min_stack.append(i)

        return result
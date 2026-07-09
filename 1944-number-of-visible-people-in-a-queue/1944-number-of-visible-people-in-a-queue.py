class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(heights))]
        n = len(heights)

        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
                res[i] += 1
            
            if stack:
                res[i] += 1
                
            stack.append(i)
        
        return res
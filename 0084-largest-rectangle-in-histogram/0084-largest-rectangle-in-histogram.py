class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        max_area = 0
        left_min_dict = {}
        right_min_dict = {}

        right_min_element = []
        for i in range(n):
            while right_min_element and heights[right_min_element[-1]] > heights[i]:
                index = right_min_element.pop()
                right_min_dict[index] = i
            
            right_min_element.append(i)
        
        while right_min_element:
            index = right_min_element.pop()
            right_min_dict[index] = n

        left_min_element = []
        for i in range(n-1, -1, -1):
            while left_min_element and heights[left_min_element[-1]] > heights[i]:
                index = left_min_element.pop()
                left_min_dict[index] = i
            
            left_min_element.append(i)
        
        while left_min_element:
            index = left_min_element.pop()
            left_min_dict[index] = -1
        

        for i in range(len(heights)):
            left_index= left_min_dict[i]
            right_index = right_min_dict[i]

            max_area = max(max_area, (right_index - left_index - 1) * heights[i])

        return max_area





  

        
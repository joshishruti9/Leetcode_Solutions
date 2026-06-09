class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        max_total_normal = float("-inf")
        total = 0


        for num in nums:
            total += num
            max_total_normal = max(max_total_normal, total)

            if total < 0:
                total = 0 

        prefix_sum_list = []
        reverse_prefix_sum_list = [float("-inf") for i in range(len(nums))]


        total = 0
        for i in range(len(nums)):
            total += nums[i]
            prefix_sum_list.append(total)
        
        total = 0
        for i in range(len(nums)-1, -1, -1):
            total += nums[i]
            reverse_prefix_sum_list[i] = total

        curr_max = float("-inf")
        curr_max_list = []
        curr_max_reverse_list = [float("-inf") for i in range(len(nums))]

        for num in prefix_sum_list:
            curr_max = max(curr_max, num)
            curr_max_list.append(curr_max)
        
        curr_max = float("-inf")
        for i in range(len(reverse_prefix_sum_list)-1, -1, -1):
            curr_max = max(curr_max, reverse_prefix_sum_list[i])
            curr_max_reverse_list[i] = curr_max

        circular_max = float("-inf")
        for i in range(len(curr_max_list)-2):
            circular_max = max(circular_max, curr_max_list[i] + curr_max_reverse_list[i+2])
        

        return max(circular_max, max_total_normal)
        


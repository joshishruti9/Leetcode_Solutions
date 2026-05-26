class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counter = Counter(nums)
        k = 0

        for i in range(3):
            count = counter[i]
            for j in range(count):
                nums[k] = i
                k += 1
        
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        n = len(nums)
        res = []

        for key, val in counter.items():
            if val > (n//3):
                res.append(key)
        return res

        
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        elevation = 0
        max_elevation = 0
        i = 0
        while i < len(gain):
            elevation += gain[i]
            max_elevation = max(max_elevation,elevation)
            i += 1
        return max_elevation 
        
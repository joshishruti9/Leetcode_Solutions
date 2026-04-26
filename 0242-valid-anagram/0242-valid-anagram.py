class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hmap = dict()

        for char in s:
            hmap[char] = hmap.get(char, 0) + 1


        for char in t:
            if char in hmap and hmap[char] > 0:
                hmap[char] -= 1
            else:
                return False
        
        for key, val in hmap.items():
            if val != 0:
                return False
        
        return True
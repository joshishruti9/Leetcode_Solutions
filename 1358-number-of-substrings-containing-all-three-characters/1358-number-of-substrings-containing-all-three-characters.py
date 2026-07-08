class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        count = 0 
        i = 0
        j = 0
        hmap = {}

        for i in range(len(s)):
            hmap[s[i]] = hmap.get(s[i], 0) + 1
                
            while len(hmap) == 3:
                
                if len(hmap) == 3:
                    count += len(s) - i
                
                hmap[s[j]] -= 1
                if hmap[s[j]] == 0:
                    hmap.pop(s[j])
                j += 1


        return count
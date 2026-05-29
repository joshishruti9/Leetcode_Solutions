class Solution:
    # start with 2 pointers i and j and iterate till j < len(s)
    # create counter for t
    # traverse through s and add values and count in hmap/dict.
    # once s has all the values with equal count calculate min_len
    # After calculating min_len decrement s[i] and remove s[i] from hmap if count == 0, increment i
    # if hmap is still same again calculate min_len.
    # continue till hmap is same after that increment j

    def match_map(self, s_counter, t_counter):

        for key, val in t_counter.items():
            if key not in s_counter or s_counter[key] < val:
                return False
        
        return True

    def minWindow(self, s: str, t: str) -> str:
        i = 0
        j = 0
        min_len = float("inf")
        s_counter = {}

        if len(s) < len(t):
            return ""
        
        if s == t:
            return s

        t_counter = Counter(t)

        while j < len(s):
            s_counter[s[j]] = s_counter.get(s[j],0) + 1
    
            while self.match_map(s_counter, t_counter):
                if (j-i) < min_len:
                    res = s[i:j+1]
                    min_len = min(min_len, j-i)
                
                s_counter[s[i]] -= 1
                if s_counter[s[i]] == 0:
                    s_counter.pop(s[i])
                
                i += 1
            
            j += 1

        return res if min_len != float("inf") else ""
        
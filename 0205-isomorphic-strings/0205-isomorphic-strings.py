class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmap = dict()
        visited =set()

        for s_char, t_char in zip(s,t):
            if s_char not in hmap:
                if t_char not in visited:
                    hmap[s_char] = t_char
                    visited.add(t_char)
                else:
                    return False
            else:
                if hmap[s_char] != t_char:
                    return False
        
        return True
        
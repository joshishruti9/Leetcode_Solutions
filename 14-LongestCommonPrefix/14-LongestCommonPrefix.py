# Last updated: 4/8/2025, 2:36:50 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j = 0
        res = []

        if len(strs) == 1:
            return strs[0]
            
        while True:
            for i in range(len(strs)-1):
                if len(strs[i]) == j or len(strs[i+1]) == j or strs[i][j] != strs[i+1][j]:
                    return "".join(res)
            res.append(strs[i][j])
            j += 1

        return "".join(res)       
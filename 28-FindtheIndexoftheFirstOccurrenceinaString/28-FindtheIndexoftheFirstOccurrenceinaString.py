class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0

        if len(needle) > len(haystack):
            return -1

        while i < (len(haystack)-j):
            if haystack[i+j] == needle[j]:
                j += 1
            else:
                i += 1
                j = 0
            if j == len(needle):
                return i
        
        return -1
# Last updated: 5/25/2025, 1:32:36 PM
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set_str = set(allowed)
        flag = False
        count = 0

        for word in words:
            for char in word:
                if char in set_str:
                    flag = True
                else:
                    flag = False
                    break

            if flag:
                count += 1
                flag= False
        
        return count
        
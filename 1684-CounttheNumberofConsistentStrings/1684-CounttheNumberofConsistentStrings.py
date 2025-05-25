# Last updated: 5/25/2025, 1:33:23 PM
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=len(words)
        allowed_set=set(allowed)
        for word in words:
            for letters in word:
                if letters not in allowed_set:
                    count-=1
                    break
                else:
                    continue
        return count
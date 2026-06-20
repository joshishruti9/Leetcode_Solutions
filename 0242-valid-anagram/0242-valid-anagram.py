class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}

        for letter in s:
            if letter in char_count:
                char_count[letter] += 1
            else:
                char_count[letter] = 1
        
        for letter in t:
            if letter in char_count:
                char_count[letter] -= 1
                if char_count[letter] == 0:
                    char_count.pop(letter)
            else:
                return False
        
        return len(char_count) == 0

        
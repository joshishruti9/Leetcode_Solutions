class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        counter = Counter(magazine)

        for letter in ransomNote:
            if letter in counter and counter[letter] > 0:
                counter[letter] -= 1
            else:
                return False
        
        return True
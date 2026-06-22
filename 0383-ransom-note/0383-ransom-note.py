class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine_counter = Counter(magazine)

        for letter in ransomNote:
            if letter in magazine_counter:
                magazine_counter[letter] -= 1
                if magazine_counter[letter] == 0:
                    magazine_counter.pop(letter)
            else:
                return False
        
        return True
        
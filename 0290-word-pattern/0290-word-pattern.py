class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        letter_to_word = {}
        word_to_letter = {}

        for i in range(len(pattern)):
            if pattern[i] in letter_to_word:
                if letter_to_word[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] not in word_to_letter:
                    letter_to_word[pattern[i]] = words[i]
                    word_to_letter[words[i]] = pattern[i]
                else:
                    return False
        
        return True
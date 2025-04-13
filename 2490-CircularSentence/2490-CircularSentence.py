# Last updated: 4/13/2025, 4:23:53 PM
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        word_arr = sentence.split(" ")
        i = 0

        if len(word_arr) == 1:
            j = len(word_arr[0]) - 1
            return word_arr[0][0] == word_arr[0][j]

        while i < len(word_arr)-1:
            j = len(word_arr[i]) - 1
            if word_arr[i][j] != word_arr[i+1][0]:
                return False 
            i += 1
        
        j = len(word_arr[i]) - 1
        if word_arr[0][0] != word_arr[i][j]:
            return False
        return True
# Last updated: 7/9/2025, 4:40:36 PM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        letters = set(brokenLetters)

        words = text.split(' ')
        count = 0
        flag = True

        for word in words:
            flag = True
            for letter in word:
                if letter in letters:
                    flag = False
                    break
            if flag:
                count += 1
            
        '''
        while i < n:
            if text[i] in letters:
                while i < n and text[i] != " ":
                    flag = False
                    i += 1
            elif text[i] not in letters:
                if text[i] == " ":
                    if flag:
                        count += 1
                        flag = False
                    i += 1
                    continue
                else:
                    flag = True
                    i += 1   
        
        if flag:
            count += 1
        '''

        return count
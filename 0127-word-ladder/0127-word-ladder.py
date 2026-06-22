from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordset = set(wordList)

        if endWord not in wordset:
            return 0
        
        word_queue = deque()
        visited = set()
        word_queue.append(beginWord)
        visited.add(beginWord)

        distance = 1

        while word_queue:
            temp_queue = []
            for curr_word in word_queue:

                if curr_word == endWord:
                    return distance
                
                for i in range(len(curr_word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        if char == curr_word[i]:
                            continue
                        
                        new_word = curr_word[:i] + char + curr_word[i+1:]
                        if new_word in wordset and new_word not in visited:
                            temp_queue.append(new_word)
                            visited.add(new_word)
            word_queue = temp_queue
            distance += 1
        

        return 0
        

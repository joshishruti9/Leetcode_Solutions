from collections import deque

class Solution:
    def get_neighbours(self, curr_gene, bank_set, queue, visited):
        char_set = set('ACGT')
        
        for i in range(len(curr_gene)):
            curr_char = curr_gene[i]
            for char in char_set:
                if curr_char != char:
                    nbr = curr_gene[:i] + char + curr_gene[i+1:]
                    if nbr in bank_set and nbr not in visited:
                        queue.append(nbr)
                        visited.add(nbr)


    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        bank_set = set(bank)
        visited = set()

        if endGene not in bank_set:
            return -1

        queue = deque()
        queue.append(startGene)
        visited.add(startGene)
        step_count = 0

        while queue:
            queue2 = []
            for curr_gene in queue:

                if curr_gene == endGene:
                    return step_count

                self.get_neighbours(curr_gene, bank_set, queue2, visited)
            
            step_count += 1
            queue = queue2
        
        return -1

        
           
                

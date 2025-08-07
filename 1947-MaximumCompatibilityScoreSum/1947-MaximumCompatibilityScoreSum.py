# Last updated: 8/7/2025, 3:24:40 PM
class Solution:
    def calculate_compatibility_score(self, student_ans, mentor_ans):
        count = 0
        for s_ans, m_ans in zip(student_ans, mentor_ans):
            if s_ans == m_ans:
                count += 1
        
        return count
    
    def find_mentor(self, mentors, student, student_index):
        student_score = {}
        for j, mentor in enumerate(mentors):
            score = self.calculate_compatibility_score(student, mentor)
            student_score[(student_index,j)] = score

        return student_score
    
    def find_max_score(self, score, visited, curr_score, student_index, n):

        if len(visited) == n:
            self.max_score = max(self.max_score, curr_score)
            return
        
        for mentor_index in range(n):
                if mentor_index not in visited: 
                    visited.add(mentor_index)
                    #print(i, " ", mentor_i, " ")
                    curr_score += score[(student_index,mentor_index)]
                    self.find_max_score(score, visited, curr_score, student_index+1, n)
                    visited.remove(mentor_index)
                    curr_score -= score[(student_index, mentor_index)]
           
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:

        score = {}
        visited = set()
        self.max_score = 0
        n = len(students)

        for i, student in enumerate(students):
            student_mentor_score = self.find_mentor(mentors, student, i)
            score.update(student_mentor_score)

        self.find_max_score(score, visited, 0, 0, n)

        return self.max_score
        
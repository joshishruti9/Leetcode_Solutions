class TopVotedCandidate:

    def bisect_left(self, low, high, value):

        while low < high:
            mid = (low + high) // 2

            if value <= self.times[mid]:
                high = mid
            else:
                low = mid + 1
        
        return low

    def __init__(self, persons: List[int], times: List[int]):
        self.n = len(times)
        self.person_vote_dict = {}
        self.vote_count  = {}
        max_count = 0
        curr_lead = 0
        self.times = times

        for i, person in enumerate(persons):
            self.vote_count[person] = self.vote_count.get(person, 0) + 1
            
            if max_count <= self.vote_count[person]:
                max_count = self.vote_count[person]
                curr_lead = person
            
            self.person_vote_dict[times[i]] = curr_lead

        print(self.person_vote_dict)
        
    def q(self, t: int) -> int:

        index = self.bisect_left(0, self.n, t)
        if index == self.n:
            return self.person_vote_dict[self.times[self.n-1]]

        if self.times[index] == t:
            return self.person_vote_dict[self.times[index]]
        return self.person_vote_dict[self.times[index-1]]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
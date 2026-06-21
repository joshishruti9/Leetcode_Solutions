class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1 for i in range(len(ratings))]

        sorted_ratings = sorted(ratings)

        index_map = {}

        for index, rating in enumerate(ratings):
            if rating not in index_map:
                index_map[rating] = [index]
            else:
                index_map[rating].append(index)
        
        for rating in sorted_ratings:
            for curr_index in index_map[rating]:

                left_small = curr_index > 0 and ratings[curr_index] > ratings[curr_index-1]
                right_small = curr_index < n-1 and ratings[curr_index] > ratings[curr_index+1]

                if left_small and right_small:
                    candies[curr_index] = max(candies[curr_index+1], candies[curr_index-1]) + 1
                elif left_small:
                    candies[curr_index] = candies[curr_index-1] + 1
                elif right_small:
                    candies[curr_index] = candies[curr_index+1] + 1
                else:
                    continue
                


        
        return sum(candies)
                    

        
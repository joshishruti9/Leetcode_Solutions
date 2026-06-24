class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False
        
        hand.sort()
        counter = Counter(hand)
        output = []

        for num in hand:
            if num in counter:
                i = 0
                res = []
                while i < groupSize and num in counter:
                    counter[num] -= 1
                    res.append(num)
                    if counter[num] == 0:
                        counter.pop(num)
                    num += 1
                    i += 1
                if i != groupSize:
                    return False
        
        return True

        

        
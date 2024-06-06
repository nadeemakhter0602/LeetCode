from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        count = Counter(hand)
        for i in hand:
            if count[i] > 0:
                for j in range(i, i + groupSize):
                    count[j] = count.get(j, 0) - 1
                    if count[j] < 0:
                        return False
        return True

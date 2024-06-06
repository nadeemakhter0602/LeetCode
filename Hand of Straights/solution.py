from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        for i in hand:
            while count[i - 1]:
                i -= 1
            if count[i] > 0:
                for j in range(i, i + groupSize):
                    count[j] -= 1
                    if count[j] < 0:
                        return False
        return True

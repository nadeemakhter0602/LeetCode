from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        for i in hand:
            start = i
            while count[start - 1]:
                start -= 1
            while start <= i:
                while count[start] > 0:
                    for j in range(start, start + groupSize):
                        count[j] -= 1
                        if count[j] < 0:
                            return False
                start += 1
        return True

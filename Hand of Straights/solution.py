class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        groups = [[] for i in range(len(hand) // groupSize)]
        for i in range(len(hand)):
            added = False
            for group in groups:
                if (not group or hand[i] - group[-1] == 1) and len(group) < groupSize:
                    added = True
                    group.append(hand[i])
                    break
            if not added:
                return False
        return True

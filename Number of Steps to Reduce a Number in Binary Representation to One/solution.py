class Solution:
    def numSteps(self, s: str) -> int:
        carry = 0
        steps = 0
        for i in range(len(s) - 1, 0, -1):
            if s[i] == "1" and carry == 0:
                carry = 1
                steps += 2
            elif s[i] == "1" and carry == 1:
                carry = 1
                steps += 1
            elif s[i] == "0" and carry == 0:
                steps += 1
            elif s[i] == "0" and carry == 1:
                carry = 1
                steps += 2
        if carry == 1:
            steps += 1
        return steps

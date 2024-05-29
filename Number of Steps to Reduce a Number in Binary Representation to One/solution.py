class Solution:
    def numSteps(self, s: str) -> int:
        carry = 0
        steps = 0
        for i in range(len(s) - 1, 0, -1):
            if not carry:
                if s[i] == "1":
                    carry = 1
                    steps += 2
                else:
                    steps += 1
            else:
                carry = 1
                if s[i] == "1":
                    steps += 1
                else:
                    steps += 2
        steps += carry
        return steps

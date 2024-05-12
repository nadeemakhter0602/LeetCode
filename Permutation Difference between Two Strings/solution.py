class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        pos = [0 for i in range(26)]
        for i in range(len(s)):
            pos[ord(s[i]) - 97] = abs(pos[ord(s[i]) - 97] - i)
            pos[ord(t[i]) - 97] = abs(pos[ord(t[i]) - 97] - i)
        return sum(pos)

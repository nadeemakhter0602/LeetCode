class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        matched_chars = 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                matched_chars += 1
                i += 1
            j += 1
        return len(t) - matched_chars

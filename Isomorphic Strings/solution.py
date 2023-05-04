class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s = dict()
        mapping_t = dict()
        tmp_t = ""
        tmp_s = ""
        for i in range(len(s)):
            if s[i] not in mapping_s:
                mapping_s[s[i]] = t[i]
            if t[i] not in mapping_t:
                mapping_t[t[i]] = s[i]
            tmp_t += mapping_s[s[i]]
            tmp_s += mapping_t[t[i]]
        return tmp_t == t and tmp_s == s

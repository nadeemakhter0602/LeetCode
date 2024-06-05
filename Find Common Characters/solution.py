from collections import Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c = Counter(words[0])
        for i in range(1, len(words)):
            word = Counter(words[i])
            keys = list(c.keys())
            for l in keys:
                if l in word:
                    c[l] = min(c[l], word[l])
                else:
                    del c[l]
        res = []
        for l in c:
            for i in range(c[l]):
                res.append(l)
        return res

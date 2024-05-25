class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)

        def backtrack(i, words, sentences):
            if i == len(s):
                sentences.append(" ".join(words))
                return
            for j in range(i, len(s)):
                word = s[i : j + 1]
                if word in wordDict:
                    backtrack(j + 1, words + [word], sentences)
            return sentences

        return backtrack(0, [], [])

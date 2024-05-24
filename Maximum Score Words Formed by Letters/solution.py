from collections import Counter
from math import prod


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        letter_count = Counter(letters)
        scores = {
            word: sum([score[ord(letter) - ord("a")] for letter in word])
            for word in words
        }

        def backtrack(i, maxScore):
            if i >= len(words):
                return 0
            maxScore = backtrack(i + 1, maxScore)
            if prod([True if letter in letter_count else False for letter in words[i]]):
                valid = True
                for letter in words[i]:
                    letter_count[letter] -= 1
                    if letter_count[letter] < 0:
                        valid = False
                if valid:
                    maxScore = max(
                        maxScore, scores[words[i]] + backtrack(i + 1, maxScore)
                    )
                for letter in words[i]:
                    letter_count[letter] += 1
            return maxScore

        return backtrack(0, 0)

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        letters = set(words[0])
        for letter in letters:
            frequency = min([word.count(letter) for word in words])
            res += [letter] * frequency
        return res

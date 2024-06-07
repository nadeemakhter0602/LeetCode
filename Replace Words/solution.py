class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        root, res, end = "", "", False
        for c in sentence:
            if c == " ":
                res += root + " "
                root, end = "", False
                continue
            if end:
                continue
            root += c
            if root in dictionary:
                end = True
        res += root
        return res

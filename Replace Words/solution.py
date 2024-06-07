class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        root = ""
        res = ""
        end = False
        for c in sentence:
            if c == " ":
                if not end:
                    res += root
                end = False
                root = ""
                res += " "
                continue
            if end:
                continue
            root += c
            if root in dictionary:
                end = True
                res += root
        if not end:
            res += root
        return res

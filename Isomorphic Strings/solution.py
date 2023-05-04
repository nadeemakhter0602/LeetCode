class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def generate_uid(string):
            mapping = dict()
            uid = []
            counter = 0
            for i in string:
                if i not in mapping:
                    mapping[i] = counter
                    counter += 1
                uid.append(mapping[i])
            return uid
        return generate_uid(s) == generate_uid(t)

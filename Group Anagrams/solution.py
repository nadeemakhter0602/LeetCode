class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        anagrams = dict()
        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c) - ord('a')] += 1
            key = str(count)
            if key not in anagrams:
                anagrams[key] = [i]
            else:
                anagrams[key].append(i)
        return anagrams.values()
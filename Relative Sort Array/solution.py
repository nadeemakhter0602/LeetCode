from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        res = []
        for i in arr2:
            for j in range(count[i]):
                res.append(i)
            del count[i]
        sec = []
        for i in count:
            for j in range(count[i]):
                sec.append(i)
        sec.sort()
        return res + sec

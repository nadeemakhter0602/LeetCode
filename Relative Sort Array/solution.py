class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        pos = dict()
        for i in range(len(arr2)):
            pos[arr2[i]] = i
        for i in arr1:
            if i not in pos:
                pos[i] = 1000 + i
        arr1.sort(key=lambda x: pos[x])
        return arr1

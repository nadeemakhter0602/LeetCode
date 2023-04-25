class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = -1
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > m:
                arr[i], m = m, arr[i]
            else:
                arr[i] = m
        return arr

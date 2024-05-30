class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        triplets = 0
        n = len(arr)
        xor = 0
        for i in range(n):
            xor = arr[i]
            for j in range(i + 1, n):
                xor ^= arr[j]
                if xor == 0:
                    triplets += j - i
        return triplets

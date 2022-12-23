class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = dict()
        f = [[] for i in range(len(nums) + 1)]
        for i in nums:
            s[i] = 1 + s.get(i, 0)
        for i in s:
            f[s[i]].append(i)
        res = []
        for i in range(len(nums), 0, -1):
            for j in f[i]:
                res.append(j)
                k -= 1
                if k == 0:
                    return res
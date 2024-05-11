import heapq


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        pairs = []
        for i in range(len(quality)):
            pairs.append((quality[i], wage[i] / quality[i]))
        pairs.sort(key=lambda x: x[1])
        total_quality = 0
        res = float("inf")
        maxHeap = []
        for q, rate in pairs:
            heapq.heappush(maxHeap, -q)
            total_quality += q
            if len(maxHeap) > k:
                total_quality += heapq.heappop(maxHeap)
            if len(maxHeap) == k:
                res = min(res, rate * total_quality)
        return res

import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        capital_min_heap = []
        profit_max_heap = []
        for i in range(len(profits)):
            heapq.heappush(capital_min_heap, (capital[i], profits[i]))
        while k > 0:
            while capital_min_heap and capital_min_heap[0][0] <= w:
                capital, profit = heapq.heappop(capital_min_heap)
                heapq.heappush(profit_max_heap, -profit)
            if not profit_max_heap:
                break
            w += -heapq.heappop(profit_max_heap)
            k -= 1
        return w

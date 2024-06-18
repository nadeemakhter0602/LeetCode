class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        max_difficulty = max(difficulty)
        difficulty_to_profit = [0 for i in range(max_difficulty + 1)]
        for i in range(len(difficulty)):
            difficulty_to_profit[difficulty[i]] = max(
                difficulty_to_profit[difficulty[i]], profit[i]
            )
        max_so_far = 0
        for i in range(max_difficulty + 1):
            max_so_far = max(difficulty_to_profit[i], max_so_far)
            difficulty_to_profit[i] = max_so_far
        max_profit = 0
        for ability in worker:
            if ability > max_difficulty:
                max_profit += difficulty_to_profit[max_difficulty]
            else:
                max_profit += difficulty_to_profit[ability]
        return max_profit

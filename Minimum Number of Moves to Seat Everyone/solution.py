class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = max(max(seats), max(students))
        differences = [0 for i in range(n)]
        for seat in seats:
            differences[seat - 1] += 1
        for student in students:
            differences[student - 1] -= 1
        moves = 0
        unmatched = 0
        for difference in differences:
            moves += abs(unmatched)
            unmatched += difference
        return moves

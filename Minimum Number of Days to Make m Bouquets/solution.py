class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def num_bouquet(day):
            flowers = 0
            bouquet = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                else:
                    flowers = 0
                if flowers == k:
                    bouquet += 1
                    flowers = 0
            return bouquet

        l = min(bloomDay)
        r = max(bloomDay)
        min_day = -1
        while l <= r:
            day = (l + r) // 2
            if num_bouquet(day) >= m:
                min_day = day
                r = day - 1
            else:
                l = day + 1
        return min_day

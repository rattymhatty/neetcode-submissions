class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate = 1
        maxRate = max(piles)
        while minRate < maxRate:
            rate = (minRate + maxRate) // 2
            hours = 0
            for num in piles:
                hours += -(-num // rate)
                if hours > h:
                    break
            if hours > h:
                minRate = rate + 1
            else:
                maxRate = rate
        return minRate
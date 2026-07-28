import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right)//2
            hours_spend = 0

            for pile in piles:
                hours_spend += math.ceil(pile/mid)
            
            if hours_spend <= h:
                right = mid
            else:
                left = mid+1

        return right
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hoursNeeded(speed):
            hours = 0

            for pile in piles:
                hours += (pile + speed - 1) // speed

            return hours

        left = 1
        right = max(piles)

        while left <= right:

            mid = (left + right) // 2

            if hoursNeeded(mid) <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left
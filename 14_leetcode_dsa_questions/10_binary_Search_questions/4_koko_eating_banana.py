from typing import List


class Solution4:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid_speed = (left + right) // 2

            hours_spent = 0
            for pile in piles:
                hours_spent += (pile + mid_speed - 1) // mid_speed

            if hours_spent <= h:
                right = mid_speed
            else:
                left = mid_speed + 1

        return left


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    hours = 8
    object = Solution4()
    print(f"Minimum number is :- {object.minEatingSpeed(piles, hours)}")

from typing import List


class Solution3:
    def kidsWithCandies(self, candies: List[int], extraCandies: int):
        result = []

        for candy in candies:
            if candy + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result


candies = [2, 3, 5, 1, 3]
extraCandies = 3
object = Solution3()
print(
    f"Child with greatest number of candies = "
    f"{object.kidsWithCandies(candies, extraCandies)}"
)

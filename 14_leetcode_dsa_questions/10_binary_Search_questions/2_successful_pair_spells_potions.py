import bisect
from typing import List


class Solution2:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        m = len(potions)
        result = []

        for s in spells:
            # calculate min portaion strength needed
            target = (success + s - 1) // s
            # Find index of first portion >= target
            index = bisect.bisect_left(potions, target)
            result.append(m - index)

        return result


if __name__ == "__main__":
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7

    object = Solution2()
    print(f"Successful pairs are :- {object.successfulPairs(
        spells, potions, success)}")

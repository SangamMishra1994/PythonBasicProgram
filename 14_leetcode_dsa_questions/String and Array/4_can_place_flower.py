# You have a long flowerbed in which some of the plots are planted,
# and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's,
# where 0 means empty and 1 means not empty,
# and an integer n, return true if n new flowers can be planted in the
# flowerbed without violating the no-adjacent-flowers rule and false otherwise.


from typing import List


class Solution4:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return n <= 0


flower = [1, 0, 0, 0, 1]
n = 1
object = Solution4()
print(f"Output will be = {object.canPlaceFlowers(flower, n)}")

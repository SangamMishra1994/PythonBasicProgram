from typing import List


class Solution3:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0

        while left < right:
            # width = right - left
            # currentHeight = min(height[left], height[right])
            # area = width * currentHeight
            # maxArea = max(area, maxArea)
            maxArea = max(maxArea, 
                          (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
object = Solution3()
print(f"Result : - {object.maxArea(height)}")

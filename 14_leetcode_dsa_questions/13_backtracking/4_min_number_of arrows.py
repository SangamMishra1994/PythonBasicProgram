from typing import List


class Solution4:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort by end
        points.sort(key=lambda x: x[1])

        arrows = 1
        last_arrow = points[0][1]

        for start, end in points[1:]:

            if start > last_arrow:
                arrows += 1
                last_arrow = end

        return arrows


if __name__ == "__main__":
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    object = Solution4()
    print(f"No of arrows to bust the ballon:- "
          f"{object.findMinArrowShots(points)}")

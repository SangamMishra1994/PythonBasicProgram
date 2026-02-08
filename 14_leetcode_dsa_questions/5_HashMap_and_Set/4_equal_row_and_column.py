from typing import List
from collections import defaultdict


class Solution4:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        row_map = defaultdict(int)

        # Step 1: store rows
        for row in grid:
            row_map[tuple(row)] += 1

        count = 0

        # Step 2: check columns
        for c in range(n):
            col = []
            for r in range(n):
                col.append(grid[r][c])

            count += row_map.get(tuple(col), 0)

        return count


# test cases
grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
# Test cases 2
# grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
object = Solution4()
print(f"Count equal row and Column : - {object.equalPairs(grid)}")

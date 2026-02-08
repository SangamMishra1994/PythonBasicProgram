from collections import defaultdict
from typing import List


class Solution2:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_of_count = defaultdict(int)

        for num in arr:
            num_of_count[num] += 1

        set_counter = set()

        for value in num_of_count.values():
            if value in set_counter:
                return False

            set_counter.add(value)

        return True


arr = [1, 2, 2, 1, 1, 3]
object = Solution2()
print(f"Is uniques occurence is present : - {object.uniqueOccurrences(arr)}")

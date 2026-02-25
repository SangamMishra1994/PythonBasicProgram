from typing import List


class Solution3:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        count = 0
        prev_end = float("-inf")

        for start, end in intervals:
            if start >= prev_end:
                count += 1
                prev_end = end
        return len(intervals) - count


if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    object = Solution3()
    print(f"Non-overlapping elements are :- "
          f"{object.eraseOverlapIntervals(intervals)}"
          )
